from fastapi import FastAPI, HTTPException
from schema.user_input import PopularBooks, SimilarBooks
from model.predict import pt, popular, similarity, recommend_similar

app = FastAPI(
    title="Book Recommendation API",
    description="Popularity & Collaborative Filtering with Confidence"
)

@app.get("/")
def home():
    return {
        "status": "Book recommender API running",
        "total_books_cf": pt.shape[0],
        "popular_books_available": len(popular)
    }

@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_loaded": similarity is not None
    }

@app.get("/books")
def get_books(limit: int = 5000):
    books = list(pt.index[:limit])
    return {
        "count": len(books),
        "books": books
    }

@app.post("/popular")
def popular_books(data: PopularBooks):
    top_df = popular.head(data.top_n)
    return {
        "type": "popularity_based",
        "count": len(top_df),
        "books": top_df.to_dict(orient="records")
    }

@app.post("/similar")
def similar_books(data: SimilarBooks):
    recommendations = recommend_similar(
        data.book_name,
        data.top_n
    )

    if not recommendations:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "type": "collaborative_filtering",
        "input_book": data.book_name,
        "recommendations": recommendations
    }
    