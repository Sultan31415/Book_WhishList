import type { Book, BookFormData } from '../types';

const API_URL = 'http://localhost:8000';

export const api = {
    async getBooks(): Promise<Book[]> {
        try {
            const response = await fetch(`${API_URL}/books`);
            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                console.error('Failed to fetch books:', errorData);
                throw new Error('Failed to fetch books');
            }
            return response.json();
        } catch (error) {
            console.error('Error fetching books:', error);
            throw error;
        }
    },

    async createBook(book: BookFormData): Promise<Book> {
        try {
            const response = await fetch(`${API_URL}/books`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(book),
            });
            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                console.error('Failed to create book:', errorData);
                throw new Error('Failed to create book');
            }
            return response.json();
        } catch (error) {
            console.error('Error creating book:', error);
            throw error;
        }
    },

    async deleteBook(id: number): Promise<Book> {
        try {
            const response = await fetch(`${API_URL}/books/${id}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                console.error('Failed to delete book:', errorData);
                throw new Error('Failed to delete book');
            }
            return response.json();
        } catch (error) {
            console.error('Error deleting book:', error);
            throw error;
        }
    },
}; 