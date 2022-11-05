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

# Items
########################################################

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# Users
########################################################

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
