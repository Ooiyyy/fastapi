from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import user_schema
from services import user_service


router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)
@router.get("/", response_model= List[user_schema.UserResponse], status_code=200)
def read_users(db : Session = Depends(get_db)):
    return user_service.getUsers(db)

@router.get("/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    result = user_service.getUserById(user_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@router.post("/", response_model=user_schema.UserResponse, status_code=201)
def store_users(new_user : user_schema.UserCreate, db : Session = Depends(get_db)):
    new_user = user_service.storeUser(new_user, db)
    return new_user

@router.put("/{user_id}", response_model= user_schema.UserResponse, status_code=200)
def update_user(user_id : int, edit_value : user_schema.UserUpdate, db : Session = Depends(get_db)):
    updated_user = user_service.updateUser(user_id, edit_value, db)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
