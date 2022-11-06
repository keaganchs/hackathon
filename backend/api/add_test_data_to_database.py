import pandas as pd
import os
from sqlalchemy.orm import Session

from .cities import create_city
from database.pydantic_models import CityCreate

def add_test_data_to_db(db: Session):
    # Assumes the current directory is */hackathon/backend/ (where the server would be started)
    try:    
        path = os.getcwd() + "\\database\\global-city-population-estimates.xls"
        df = pd.read_excel(path, sheet_name="CITIES-OVER-300K", usecols="B,D,F,G,V")
    except:
        raise SystemError("Unable to open Excel data file.")

    for _, row_entry in df.iterrows():
        # Parse data 
        new_city = CityCreate(
            country     = row_entry["Country or area"],
            city        = row_entry["Urban Agglomeration"],
            longitude   = row_entry["Longitude"],
            latitude    = row_entry["Latitude"],
            population  = round(row_entry["2020"] * 1000)
        )

        # Add new_city to database
        create_city(
            db=db,
            city=new_city
        )

# if __name__ == "__main__":
#     # Assumes this file is run from the directory where it is located
#     path = os.getcwd() + "\\..\\database\\global-city-population-estimates.xls"
#     df = pd.read_excel(path, sheet_name="CITIES-OVER-300K", index_col=0, usecols="B,D,F,G,V")
#     print(df.head())