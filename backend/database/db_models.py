from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, BLOB
from sqlalchemy.orm import relationship

from .database import Base

class City(Base):
    __tablename__ = "cities"

    id              = Column(Integer, primary_key=True, index=True)
    country         = Column(String(64))
    city            = Column(String(128))
    longitude       = Column(Float)
    latitude        = Column(Float)
    population      = Column(Integer)

class Map(Base):
    __tablename__ = "maps"

    id              = Column(Integer, primary_key=True, index=True)
    first_city      = Column(String(128))
    second_city     = Column(String(128))
    map_image       = Column(BLOB())
