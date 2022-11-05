from sqlalchemy.orm import Session

from database import db_models, pydantic_models


def get_user(db: Session, user_id: int):
    return db.query(db_models.User).filter(db_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(db_models.User).filter(db_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: pydantic_models.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: pydantic_models.ItemCreate, user_id: int):
    db_item = db_models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
