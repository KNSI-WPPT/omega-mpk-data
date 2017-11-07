import datetime

from sqlalchemy import Column, Integer, String, Time, Date, DateTime, Float, ForeignKey, PrimaryKeyConstraint

from crawlers.database import Base


class SchedulesMeta(Base):
    __tablename__ = "schedules_meta"

    resource_hash = Column(String(40), primary_key=True, nullable=False)
    load_timestamp = Column(DateTime, nullable=False)
    resource_source = Column(String(64), nullable=False)


class Agency(Base):
    __tablename__ = "agency"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    agency_id = Column(Integer, nullable=False)
    agency_name = Column(String(128))
    agency_url = Column(String(128))
    agency_timezone = Column(String(128))
    agency_phone = Column(String(128))
    agency_lang = Column(String(16))


class Calendar(Base):
    __tablename__ = "calendar"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    service_id = Column(Integer, nullable=False)
    monday = Column(Integer)
    tuesday = Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)
    sunday = Column(Integer)
    start_date = Column(Date)  # Convert from raw
    end_date = Column(Date)  # Convert from raw


class CalendarDates(Base):
    __tablename__ = "calendar_dates"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    service_id = Column(Integer, nullable=False)
    date = Column(Date)  # Convert from raw
    exception_type = Column(Integer)


class ControlStops(Base):
    __tablename__ = "control_stops"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    variant_id = Column(Integer)
    stop_id = Column(Integer)


class FeedInfo(Base):
    __tablename__ = "feed_info"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    feed_publisher_name = Column(String(128))
    feed_publisher_url = Column(String(128))
    feed_lang = Column(String(16))
    feed_start_date = Column(Date)  # Convert from raw
    feed_end_date = Column(Date)  # Convert from raw


class Routes(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    route_id = Column(String(64), nullable=False)
    agency_id = Column(Integer, nullable=False)
    route_short_name = Column(String(16))
    route_long_name = Column(String(16))
    route_desc = Column(String(1024))
    route_type = Column(Integer)
    route_type2_id = Column(Integer)
    valid_from = Column(Date)  # Convert from raw
    valid_until = Column(Date)  # Convert from raw


class RouteTypes(Base):
    __tablename__ = "route_types"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    route_type2_id = Column(Integer, nullable=False)
    route_type2_name = Column(String(128), nullable=False)


class Stops(Base):
    __tablename__ = "stops"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    stop_id = Column(Integer, nullable=False)
    stop_code = Column(Integer, nullable=False)
    stop_name = Column(String(128), nullable=False)
    stop_lat = Column(Float, nullable=False)
    stop_lon = Column(Float, nullable=False)


class StopTimes(Base):
    __tablename__ = "stop_times"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    trip_id = Column(String(32), nullable=False)
    arrival_time = Column(Time)
    departure_time = Column(Time)
    stop_id = Column(Integer)
    stop_sequence = Column(Integer)
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)


class Trips(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    route_id = Column(String(64))
    service_id = Column(Integer)
    trip_id = Column(String(32))
    trip_headsign = Column(String(128))
    direction_id = Column(Integer)
    brigade_id = Column(Integer)
    vehicle_id = Column(Integer)
    variant_id = Column(Integer)


class Variants(Base):
    __tablename__ = "variants"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    variant_id = Column(Integer)
    is_main = Column(Integer)
    equiv_main_variant_id = Column(Integer)
    join_stop_id = Column(Integer)
    disjoin_stop_id = Column(Integer)


class VehicleTypes(Base):
    __tablename__ = "vehicle_types"

    id = Column(Integer, primary_key=True)
    resource_hash = Column(String(40))

    vehicle_type_id = Column(Integer)
    vehicle_type_name = Column(String(128))
    vehicle_type_description = Column(String(256))
    vehicle_type_symbol = Column(String(32))
