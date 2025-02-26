from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
from data_loader import load_movies, load_ratings
from recommender import get_recommendations

app = FastAPI(
    title="Personalized Movie Recommendation API",
    description="API for generating movie recommendations using collaborative, content-based, and hybrid methods.",
    version="1.0.0"
)

# Enable CORS for testing.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once at startup.
movies = load_movies()
ratings = load_ratings()

@app.get("/recommendations/{user_id}")
def recommendations(user_id: int, method: str = Query("hybrid", enum=["collaborative", "content", "hybrid"]), top_n: int = 10):
    """
    Retrieve movie recommendations for a given user.
    
    - **user_id**: ID of the user.
    - **method**: Recommendation method (collaborative, content, or hybrid).
    - **top_n**: Number of recommendations to return.
    """
    try:
        recs = get_recommendations(user_id, movies, ratings, method=method, top_n=top_n)
        if recs.empty:
            raise HTTPException(status_code=404, detail="No recommendations found.")
        return recs.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
