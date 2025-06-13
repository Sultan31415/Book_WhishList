import React from 'react';
import './DailyNews.css';

const DailyNews: React.FC = () => {
  return (
    <section className="daily-news">
      <div className="daily-news__header">
        <h2>Daily Book Discoveries</h2>
        <p>Explore today's featured books from Google Books</p>
      </div>
      
      <div className="daily-news__grid">
        {/* Placeholder for book cards - will be populated with API data */}
        <div className="book-card">
          <div className="book-card__image-placeholder">
            <span>Book Cover</span>
          </div>
          <div className="book-card__content">
            <h3>Book Title</h3>
            <p className="book-card__author">Author Name</p>
            <p className="book-card__description">
              Book description will appear here...
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default DailyNews; 