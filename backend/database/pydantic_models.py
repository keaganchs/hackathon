from typing import Union

from sqlalchemy import BLOB

from pydantic import BaseModel

# Cities
########################################################

class CityBase(BaseModel):
    country: str
    city: str
    longitude: float
    latitude: float
    population: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode = True

# Maps
########################################################

class MapBase(BaseModel):
    first_country   = str
    second_country  = str
    map_image       = BLOB
    
class MapCreate(MapBase):
    pass

class Map(MapBase):
    id: int
    
    class Config:
        orm_mode = True
