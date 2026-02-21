import joblib
import pandas as pd

pt = joblib.load("model/pivot_table.joblib")
similarity = joblib.load("model/similarity.joblib", mmap_mode="r")
popular = joblib.load("model/popularity.joblib")

def recommend_similar(book_name: str, top_n: int = 10):
    if book_name not in pt.index:
        return []

    index = pt.index.get_loc(book_name)
    similarity_scores = list(enumerate(similarity[index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:top_n + 1]

    recommendations = []

    for i, score in similarity_scores:
        recommendations.append({
            "book_name": pt.index[i],
            "confidence": round(score * 100, 2) 
        })

    return recommendations
