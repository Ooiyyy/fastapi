from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import book_schema
from controllers import book_controller

router = APIRouter(
    prefix="/api/books",
    tags=["books"],
)

@router.post("/", response_model=book_schema.BookResponse)
def create_book(book: book_schema.BookCreate, db: Session = Depends(get_db)):
    return book_controller.create_book(db=db, book=book)

@router.get("/", response_model=List[book_schema.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_controller.get_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=book_schema.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_controller.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=book_schema.BookResponse)
def update_book(book_id: int, book: book_schema.BookUpdate, db: Session = Depends(get_db)):
    db_book = book_controller.update_book(db, book_id=book_id, book_update=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_controller.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
