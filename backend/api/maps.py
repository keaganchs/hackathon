from sqlalchemy.orm import Session
from typing import List

from database import db_models, pydantic_models

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
        return result

    first_city = get_city_by_name(first_city_name)
    second_city = get_city_by_name(second_city_name)
    
    fig = generator.generate_map_figure(
        country1        = first_city.country, 
        city1           = first_city.city, 
        lon1            = first_city.longitude, 
        lat1            = first_city.latitude, 
        pop1            = first_city.population, 

        country2        = second_city.country, 
        city2           = second_city.city, 
        lon2            = second_city.longitude, 
        lat2            = second_city.latitude, 
        pop2            = second_city.population 
    )

    db_map = db_models.Map(
        first_city      = first_city.city,
        second_city     = second_city.city,
        map_image       = fig
    )
    db.add(db_map)
    db.commit()
    db.refresh(db_map)

    return db_map
