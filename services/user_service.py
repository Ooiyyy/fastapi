from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.user_model import User
from schemas import user_schema


def getUsers(db : Session):
    allUser = db.query(User).all()
    return allUser

def getUserById(user_id : int,db :Session):
    user = db.query(User).filter(User.id == user_id).first()
    return user

def storeUser(value : user_schema.UserCreate, db: Session):
    new_user = User(**value.model_dump())

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="email already exists")
    return new_user

def updateUser(user_id :int, edit_value : user_schema.UserUpdate, db : Session):
    updated_user = db.query(User).filter(User.id == user_id).first()
    if updated_user:
        updated_data = edit_value.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(updated_user, key, value)
        db.commit()
        db.refresh(updated_user)
    return updated_user