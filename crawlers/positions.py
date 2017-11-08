from sqlalchemy.orm import sessionmaker

import time
import datetime
import requests
import threading

from crawlers.db.positions import Position
from crawlers.db.schedules import Routes
from crawlers.database import engine


URL = 'http://mpk.wroc.pl/position.php'

Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()


trams = None
buses = None


def update_vehicle_list():
    print("Positions -- update vehicle list")

    global trams, buses
    trams = [x[0] for x in session.query(Routes.route_id).filter(Routes.agency_id == 3).distinct()]
    buses = [x[0] for x in session.query(Routes.route_id).filter(Routes.agency_id == 2).distinct()]


def fetch_data():
    #print("Positions -- Fetching")

    now = datetime.datetime.now()

    r = requests.post(
        URL,
        data={"busList[bus][]": buses, "busList[tram][]": trams},
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    positions = r.json()
    for p in positions:
        p['datetime'] = now

    connection.execute(
        Position.__table__.insert(),
        positions
    )
