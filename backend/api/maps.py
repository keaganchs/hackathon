import pickle
from io import BytesIO
from typing import List

import matplotlib.pyplot as plt
from database import db_models, pydantic_models
from sqlalchemy.orm import Session

from .cities import get_city_by_name
from .generator import generator


# Map will be created if it is not found in the database
def get_map(db: Session, first_city_name: str, second_city_name: str) -> pydantic_models.Map:
    # Only return first result. Good to do in the future would be to let the user swap between all maps which satisfy the constraint.
    try:
        result = db.query(db_models.Map).filter(db_models.Map.first_city == first_city_name and db_models.Map.second_city == second_city_name).first()
    except:
        pass

    if result:
        # return result
        pass

    first_city = get_city_by_name(db, first_city_name)
    second_city = get_city_by_name(db, second_city_name)

    print(first_city)
    print(second_city)
    
    fig = plt.figure()
    fig = generator.generate_map_figure(
        lon1            = first_city.longitude, 
        lat1            = first_city.latitude, 
        pop1            = first_city.population, 

        lon2            = second_city.longitude, 
        lat2            = second_city.latitude, 
        pop2            = second_city.population 
    )

    db_map = db_models.Map(
        first_city      = first_city.city,
        second_city     = second_city.city,
        map_image       = bytearray("", encoding="UTF-8") # @TODO
    )
    db.add(db_map)
    db.commit()
    db.refresh(db_map)

    return db_map

def get_maps(db: Session, skip: int = 0, limit: int = 100) -> List[pydantic_models.Map]:
    return db.query(db_models.Map).offset(skip).limit(limit).all()

def delete_map(db: Session, map_id: int):
    try:
        return db.query(db_models.Map).filter(db_models.Map.id == map_id).delete()
    except:
        return "Unable to delete."