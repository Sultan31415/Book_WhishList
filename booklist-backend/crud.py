import json
from redis_client import redis_client
from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

CACHE_KEY = "books:all"
CACHE_TTL = 60  # кеш живёт 60 секунд

def get_books(db: Session):
    cached = redis_client.get(CACHE_KEY)
    if cached:
        print("🔥 Redis hit")
        return json.loads(cached)  # Вернём данные из кеша

    print("❄️ Redis miss. Querying DB.")
    books = db.query(Book).all()
    books_data = [{"id": b.id, "title": b.title, "author": b.author} for b in books]

    redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(books_data))
    return books_data

def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    redis_client.delete(CACHE_KEY)  # Invalidate cache
    return {"id": db_book.id, "title": db_book.title, "author": db_book.author}

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        redis_client.delete(CACHE_KEY)  # Invalidate cache
        return {"id": book.id, "title": book.title, "author": book.author}
    return None
