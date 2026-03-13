from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class BookResponse(BookBase):
    id: int

    # Allows Pydantic models to read ORM objects directly
    model_config = ConfigDict(from_attributes=True)
