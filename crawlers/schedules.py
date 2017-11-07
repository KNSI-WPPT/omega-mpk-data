from sqlalchemy.orm import sessionmaker

from crawlers.db.schedules import *
from crawlers.database import engine

import csv
import io
import zipfile
import datetime

import hashlib

import requests

# Session class
Session = sessionmaker(bind=engine)
connection = engine.connect()
URL = 'http://www.wroclaw.pl/open-data/opendata/rozklady/OtwartyWroclaw_rozklad_jazdy_GTFS.zip'
TABLES = [Trips, Variants, VehicleTypes, Agency, CalendarDates, Calendar, ControlStops, FeedInfo, RouteTypes, Routes, StopTimes, Stops]


def convert_rows_type(rows):
    first_row = rows[0]

    columns_to_convert = [
        (column, function)
        for column in first_row
        for keyword, function
        in [
            ("date", lambda x: datetime.datetime.strptime(str(x), "%Y%m%d").date()),
            ("valid", lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date()),
            ("time", lambda x: datetime.datetime.strptime(x, "%H:%M:%S").time())
        ]
        if column.endswith(keyword) or column.startswith(keyword)
    ]

    for row in rows:
        for column, value in row.items():
            if value.strip() == "":
                row[column] = None

    if not columns_to_convert:
        return

    for row in rows:
        for column, function in columns_to_convert:
            try:
                row[column] = function(row[column])
            except Exception as e:
                row[column] = None


def fetch_data():
    print("Schedules -- fetching")
    # Get zip archive
    request = requests.get(URL)
    archive = zipfile.ZipFile(io.BytesIO(request.content))
    print("Schedules -- Archive downloaded")

    # SQL Session
    session = Session()

    for cls in TABLES:
        with archive.open(cls.__tablename__ + ".txt") as f:
            raw = f.read()

        in_hash = hashlib.sha1(raw).hexdigest()

        last_obj = session.query(SchedulesMeta) \
            .filter(SchedulesMeta.resource_source == cls.__tablename__) \
            .order_by(SchedulesMeta.load_timestamp.desc()) \
            .first()

        if last_obj is None or last_obj.resource_hash != in_hash:
            print("Schedules -- {}".format(cls.__tablename__))

            # Read csv
            reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
            rows = list(reader)
            for row in rows:
                row["resource_hash"] = in_hash

            # Convert data types
            convert_rows_type(rows)

            connection.execute(
                SchedulesMeta.__table__.insert(),
                [{
                    "resource_hash": in_hash,
                    "load_timestamp": datetime.datetime.utcnow(),
                    "resource_source": cls.__tablename__
                }]
            )

            chunk = 5000
            for i in range((len(rows) // chunk) + 1):
                begin, end = i * chunk, min((i+1) * chunk, len(rows))
                print("Schedules -- inserting [{}:{}] {}".format(begin, end, cls.__tablename__))
                connection.execute(
                    cls.__table__.insert(),
                    rows[begin: end]
                )
        else:
            print("Schedules -- no insert {}".format(cls.__tablename__))
