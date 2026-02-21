# Book Recommendation System

A book recommendation system built using **FastAPI** and **Streamlit**.  
It provides:
- Popularity-based book recommendations  
- Similar book recommendations using collaborative filtering  
- Confidence score for each recommendation  

The entire project is containerized using **Docker** for easy setup and reproducibility.

---

## How to Run (Using Docker)

### Prerequisites
- Docker Desktop installed and running

### Steps
```bash
docker-compose up --build

Access

Streamlit UI: http://localhost:8501

FastAPI Docs: http://localhost:8000/docs

No local Python or virtual environment setup is required.
