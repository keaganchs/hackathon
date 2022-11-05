import uvicorn
from api import users
from database import db_models, pydantic_models
from database.database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

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

@app.get("/", status_code=307, response_class=RedirectResponse, tags={"redirect_root"})
def root():
    return RedirectResponse(url="/docs")

@app.get("/get", status_code=200, tags={"return_data"})
def return_data():
    return JSONResponse({"response": "Oonga Boonga"})

@app.post("/send/{favorite_number}", status_code=201, tags={"accept_data"})
def accept_data(favorite_number: int):
    new_number = favorite_number + 3
    return JSONResponse({"response": f"A better number than {favorite_number} is {new_number}"})

# Users
########################################################

@app.post("/users/", response_model=pydantic_models.User, tags={"users"})
def create_user(user: pydantic_models.UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db=db, user=user)


@app.get("/users/", response_model=list[pydantic_models.User], tags={"users"})
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return users.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}", response_model=pydantic_models.User, tags={"users"})
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=pydantic_models.Item, tags={"users"})
def create_item_for_user(
    user_id: int, item: pydantic_models.ItemCreate, db: Session = Depends(get_db)
):
    return users.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[pydantic_models.Item], tags={"users"})
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = users.get_items(db, skip=skip, limit=limit)
    return items


########################################################
#                    Start Server                      #
########################################################

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="127.0.0.1", port=8000, reload=True)