import { useState, useEffect } from 'react';
import type { Book, BookFormData } from '../types';
import { api } from '../services/api';

const BookList = () => {
    const [books, setBooks] = useState<Book[]>([]);
    const [newBook, setNewBook] = useState<BookFormData>({ title: '', author: '' });
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadBooks();
    }, []);

    const loadBooks = async () => {
        try {
            setLoading(true);
            const data = await api.getBooks();
            setBooks(data);
            setError(null);
        } catch (err) {
            setError('Failed to load books');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleAddBook = async (e: React.FormEvent) => {
        e.preventDefault();
        if (newBook.title && newBook.author) {
            try {
                const book = await api.createBook(newBook);
                setBooks([...books, book]);
                setNewBook({ title: '', author: '' });
                setError(null);
            } catch (err) {
                setError('Failed to add book');
                console.error(err);
            }
        }
    };

    const handleDeleteBook = async (id: number) => {
        try {
            await api.deleteBook(id);
            setBooks(books.filter(book => book.id !== id));
            setError(null);
        } catch (err) {
            setError('Failed to delete book');
            console.error(err);
        }
    };

    if (loading) {
        return <div className="loading">Loading books...</div>;
    }

    return (
        <div className="book-list">
            <h1>My Book List</h1>
            
            {error && <div className="error-message">{error}</div>}
            
            <form onSubmit={handleAddBook} className="add-book-form">
                <input
                    type="text"
                    placeholder="Book Title"
                    value={newBook.title}
                    onChange={(e) => setNewBook({ ...newBook, title: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Author"
                    value={newBook.author}
                    onChange={(e) => setNewBook({ ...newBook, author: e.target.value })}
                />
                <button type="submit">Add Book</button>
            </form>

            <div className="books">
                {books.map((book) => (
                    <div key={book.id} className="book-item">
                        <div className="book-info">
                            <h3>{book.title}</h3>
                            <p>by {book.author}</p>
                        </div>
                        <button 
                            onClick={() => handleDeleteBook(book.id)}
                            className="delete-btn"
                        >
                            Delete
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default BookList; 