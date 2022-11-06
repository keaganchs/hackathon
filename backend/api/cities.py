from sqlalchemy.orm import Session
from typing import List

from database import db_models, pydantic_models

def get_city(db: Session, city_id: int) -> pydantic_models.City:
    return db.query(db_models.City).filter(db_models.City.id == city_id).first()

def get_city_by_name(db: Session, city_name: str) -> pydantic_models.City:
    return db.query(db_models.City).filter(db_models.City.city == city_name).first()

def get_cities(db: Session, skip: int = 0, limit: int = 100) -> List[pydantic_models.City]:
    return db.query(db_models.City).offset(skip).limit(limit).all()

def create_city(db: Session, city: pydantic_models.CityCreate):
    db_city = db_models.City(
        country     = city.country,
        city        = city.city,
        longitude   = city.longitude,
        latitude    = city.latitude,
        population  = city.population
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def autocomplete_city_name(db: Session, term: str):
    return db.query(db_models.City).filter(db_models.City.city.contains(term)).limit(5).all()
