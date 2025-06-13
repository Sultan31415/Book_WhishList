import BookList from './components/BookList'
import DailyNews from './components/DailyNews'
import './App.css'

function App() {
  return (
    <div className="app">
      <main className="main-content">
        <BookList />
      </main>
      <aside className="daily-news-container">
        <DailyNews />
      </aside>
    </div>
  )
}

export default App
