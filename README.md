# 📚 BookList App

A full-stack BookList application built with **FastAPI** (backend), **React + Vite** (frontend), and **PostgreSQL** (database). Users can add, view, and delete books. Designed to be simple, fast, and containerized with Docker.

---

## 🚀 Features

- 📖 Add, view, and delete books
- 🔗 REST API with FastAPI
- ⚛️ React + Vite frontend
- 🐘 PostgreSQL database
- 🐳 Fully dockerized (frontend, backend, DB)
- 🔄 CI with GitHub Actions for backend and frontend

---

## 🧱 Tech Stack

| Layer     | Tech               |
|-----------|--------------------|
| Frontend  | React + Vite       |
| Backend   | FastAPI + SQLAlchemy |
| Database  | PostgreSQL         |
| DevOps    | Docker + GitHub Actions |

---

## 🧪 CI/CD with GitHub Actions

- **CI** is triggered on every push or pull request to `main`.
- Backend and frontend jobs:
  - Install dependencies
  - Run tests (if found)
  - Fail if something breaks

✅ Status badges (optional if you want to show them):
```md
![Frontend CI](https://github.com/YOUR_USERNAME/booklist/actions/workflows/ci.yml/badge.svg?branch=main)
