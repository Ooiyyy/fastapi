from sqlalchemy.orm import Session
from models.book_model import Book
from schemas.book_schema import BookCreate, BookUpdate

def get_books(skip: int = 0, limit: int = 100, db: Session = None):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book(book_id: int, db: Session = None):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(book: BookCreate, db: Session = None):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(book_id: int, book_update: BookUpdate, db: Session = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        update_data = book_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(book_id: int, db: Session = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
