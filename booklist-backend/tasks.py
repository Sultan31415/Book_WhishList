from celery_worker import celery_app
from database import SessionLocal
from models import Book
from redis_client import redis_client
import json

CACHE_KEY = "books:all"
CACHE_TTL = 60

@celery_app.task
def update_books_cache():
    db = SessionLocal()
    books = db.query(Book).all()
    books_data = [{"id": b.id, "title": b.title, "author": b.author} for b in books]
    redis_client.setex(CACHE_KEY, CACHE_TTL, json.dumps(books_data))
    db.close()
