from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base, init_db
import crud, schemas
import logging
from google_books import GoogleBooksAPI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    logger.info(f"Retrieved {len(books)} books from database")
    return books

@app.post("/books", response_model=schemas.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating new book: {book.title} by {book.author}")
    return crud.create_book(db, book)

@app.delete("/books/{book_id}", response_model=schemas.Book)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting book with id: {book_id}")
    return crud.delete_book(db, book_id)

@app.get("/daily-discoveries")
def get_daily_discoveries():
    """
    Get daily book discoveries from Google Books API
    """
    google_books = GoogleBooksAPI()
    books = google_books.get_daily_discoveries()
    logger.info(f"Retrieved {len(books)} daily book discoveries")
    return books
