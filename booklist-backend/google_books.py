import os
import requests
from typing import List, Dict, Any

class GoogleBooksAPI:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_BOOKS_API_KEY')
        self.base_url = 'https://www.googleapis.com/books/v1/volumes'
    
    def get_daily_discoveries(self, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Get daily book discoveries using random search terms
        """
        # List of popular book categories for random selection
        categories = [
            'fiction', 'science', 'history', 'biography', 'technology',
            'philosophy', 'art', 'music', 'travel', 'cooking'
        ]
        
        import random
        search_term = random.choice(categories)
        
        params = {
            'q': search_term,
            'maxResults': max_results,
            'key': self.api_key,
            'orderBy': 'newest'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            books = []
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                book = {
                    'id': item.get('id'),
                    'title': volume_info.get('title'),
                    'authors': volume_info.get('authors', ['Unknown Author']),
                    'description': volume_info.get('description', 'No description available'),
                    'image_url': volume_info.get('imageLinks', {}).get('thumbnail'),
                    'published_date': volume_info.get('publishedDate'),
                    'categories': volume_info.get('categories', []),
                }
                books.append(book)
            
            return books
        except requests.RequestException as e:
            print(f"Error fetching books from Google Books API: {e}")
            return [] 