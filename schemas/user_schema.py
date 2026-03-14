from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name : str
    address : str
    email : str
    born_date : datetime

class UserCreate(UserBase):
        pass

class UserUpdate(BaseModel):
    name : Optional [str] = None
    address : Optional [str] = None
    email : Optional [str] = None
    born_date : Optional [datetime] = None

class UserResponse(UserBase):
     id : int

model_config = ConfigDict(from_attributes=True)
