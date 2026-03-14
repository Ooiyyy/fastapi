from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import book_schema
from services import book_service

router = APIRouter(
    prefix="/api/books",
    tags=["books"],
)

@router.post("/", response_model=book_schema.BookResponse, status_code=201)
def create_book(book: book_schema.BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(book, db)

@router.get("/", response_model=List[book_schema.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_service.get_books(skip, limit, db)

@router.get("/{book_id}", response_model=book_schema.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.get_book(book_id, db)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=book_schema.BookResponse)
def update_book(book_id: int, book: book_schema.BookUpdate, db: Session = Depends(get_db)):
    db_book = book_service.update_book(book_id, book, db)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_service.delete_book(book_id, db)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
