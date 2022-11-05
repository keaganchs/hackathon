from typing import List

import uvicorn
from api import cities
from database import db_models, pydantic_models
from database.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from api.add_test_data_to_database import add_test_data_to_db

########################################################
#                        Setup                         #
########################################################

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

########################################################
#                       Routes                         #
########################################################

# General
########################################################

@app.get("/", status_code=307, response_class=RedirectResponse, tags={"Setup"})
def root():
    return RedirectResponse(url="/docs")

@app.get("/add-test-data", status_code=200, tags={"Setup"})
def add_test_data(db: Session = Depends(get_db)):
    try:
        add_test_data_to_db(db=db)
        return "Success"
    except:
        return "Unable to add test data."

# Cities
########################################################

@app.get("/cities/", response_model=List[pydantic_models.City], tags={"Cities"})
def get_all_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return cities.get_cities(db=db, skip=skip, limit=limit)

@app.get("/cities/{city_id}", response_model=pydantic_models.City, tags={"Cities"})
def get_city_by_id(city_id: int, db: Session = Depends(get_db)):
    return cities.get_city(db=db, city_id=city_id)

@app.post("/cities/create", response_model=pydantic_models.City, tags={"Cities"})
def create_city(city: pydantic_models.CityCreate, db: Session = Depends(get_db)):
    return cities.create_city(db=db, city=city)

@app.post("/cities/autocomplete", tags={"Cities"})
def autocomplete_city_name(term: str, db: Session = Depends(get_db)):
    return cities.autocomplete_city_name(db=db, term=term)

########################################################
#                    Start Server                      #
########################################################

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="127.0.0.1", port=8000, reload=True)