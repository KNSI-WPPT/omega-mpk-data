from sqlalchemy import Column, Integer, String, DateTime, Float

from crawlers.database import Base


class Position(Base):
    __tablename__ = "vehicle_positions"

    id = Column(Integer, primary_key=True, nullable=False)
    datetime = Column(DateTime)
    name = Column(String(16))
    type = Column(String(16))
    x = Column(Float)
    y = Column(Float)
    k = Column(Float)