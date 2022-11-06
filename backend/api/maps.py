from sqlalchemy.orm import Session
from typing import List

from fastapi.responses import FileResponse

from database import db_models, pydantic_models

def get_map(db: Session, city_id: int):
    return db.query(db_models.City).filter(db_models.City.id == city_id).first()

def generate_map(db: Session, map):
    # db_city = db_models.City(
    #     country     = city.country,
    #     city        = city.city,
    #     longitude   = city.longitude,
    #     latitude    = city.latitude,
    #     population  = city.population
    # )
    # db.add(db_city)
    # db.commit()
    # db.refresh(db_city)
    # return db_city
    pass


def fetch_map():
    try:
        pass
    except:
        generate_map()
