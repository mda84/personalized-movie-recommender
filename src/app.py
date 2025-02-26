from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from data_loader import load_movies, load_ratings
from recommender import get_recommendations

app = FastAPI(title="Personalized Movie Recommendation Web App")
templates = Jinja2Templates(directory="templates")

# Load data once.
movies = load_movies()
ratings = load_ratings()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the homepage with a form to input a user ID and select the recommendation method.
    """
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": None})

@app.post("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, user_id: int = Form(...), method: str = Form("hybrid")):
    """
    Process the form submission and display recommendations.
    """
    try:
        recs = get_recommendations(user_id, movies, ratings, method=method, top_n=10)
        recs_list = recs.to_dict(orient="records")
    except Exception as e:
        recs_list = []
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": recs_list, "user_id": user_id, "method": method})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
