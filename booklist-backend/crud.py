from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def get_books(db: Session):
    return db.query(Book).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book 
