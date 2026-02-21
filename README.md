# Book Recommendation System

A book recommendation system built using **FastAPI** and **Streamlit**, based on collaborative filtering.  
The project is fully containerized using **Docker**.

---

## How to Run

### Using Docker Compose
```bash
docker-compose up --build

### Run from Docker Hub
```bash
docker pull wizard2402/book-recommender:latest
docker run -p 8000:8000 -p 8501:8501 wizard2402/book-recommender:latest

## Access
```bash
Streamlit UI: http://localhost:8501
FastAPI Docs: http://localhost:8000/docs