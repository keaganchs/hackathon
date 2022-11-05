from typing import Union

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

