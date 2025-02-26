# Personalized Movie Recommendation System

## Overview
The Personalized Movie Recommendation System is a web-based application that provides tailored movie suggestions based on user preferences and past interactions. Leveraging a combination of collaborative filtering, content-based filtering, and hybrid recommendation techniques, this project demonstrates your expertise in recommender systems, data analysis, NLP, and MLOps.

The system uses a publicly available dataset (e.g., MovieLens) to build and evaluate different recommendation models. It also includes a simple web interface built with Flask (or FastAPI) and integrated visualization components to display recommendations and underlying data insights.

## Features
- **Data Ingestion & Preprocessing:**  
  - Load and preprocess movie ratings, metadata, and user reviews.
  - Handle missing values, normalize ratings, and extract textual features from movie descriptions or reviews.

- **Recommendation Algorithms:**  
  - **Collaborative Filtering:** Compute user-based and item-based similarities.
  - **Content-Based Filtering:** Leverage movie metadata and NLP techniques (TF-IDF, embeddings) to recommend similar movies.
  - **Hybrid Approach:** Combine multiple recommendation strategies to improve prediction accuracy.

- **Model Evaluation & Tuning:**  
  - Evaluate recommendation performance using metrics like RMSE, MAE, and precision/recall.
  - Perform hyperparameter tuning and cross-validation for optimal model performance.

- **Web Interface & API:**  
  - A responsive web UI for users to input ratings and view recommendations.
  - RESTful API endpoints for fetching recommendations and model insights.

- **MLOps Integration:**  
  - Version control for models.
  - CI/CD integration for automated testing and deployment.
  - Logging and monitoring of model performance in production.

## Project Structure
```
personalized-movie-recommender/
├── README.md
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml                # CI/CD pipeline configuration
├── data/
│   ├── movies.csv                # Movie metadata (columns: movieId, title, genres, description)
│   ├── ratings.csv               # User ratings (columns: userId, movieId, rating, timestamp)
│   └── reviews.csv               # (Optional) User reviews for additional NLP analysis
├── notebooks/
│   ├── Data_Preprocessing.ipynb  # Data ingestion, cleaning, and EDA
│   └── Model_Development.ipynb   # Recommendation model development and evaluation
└── src/
    ├── data_loader.py            # Functions for loading and preprocessing data
    ├── recommender.py            # Implementation of recommendation algorithms
    ├── evaluation.py             # Evaluation metrics (RMSE, MAE)
    ├── convert_movies.py
    ├── convert_ratings.py
    ├── create_dummy_reviews.py
    ├── api.py                    # FastAPI endpoints for recommendations
    └── app.py                    # Main web application with a simple HTML UI
└── templates/
    └── index.html                # HTML template for the web app
```

## Installation
### Clone the Repository
```
git clone https://github.com/yourusername/personalized-movie-recommender.git
cd personalized-movie-recommender
```
### Set Up Virtual Environment and Install Dependencies
```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Run the Web Application
```
python src/app.py
```
Open your browser and navigate to http://127.0.0.1:5000 (or the appropriate port) to access the recommendation interface.

### Docker Deployment
```
Build and run the Docker container with:
docker build -t personalized-movie-recommender .
docker run -p 5000:5000 personalized-movie-recommender
```

## Notebooks
Data_Preprocessing.ipynb:
Walks through loading raw datasets, cleaning data, feature extraction from text (e.g., movie overviews or reviews), and exploratory data analysis.

Model_Development.ipynb:
Demonstrates the development and evaluation of various recommendation algorithms, including collaborative filtering, content-based, and hybrid methods. It also covers model tuning and evaluation metrics.

## CI/CD Integration
A sample GitHub Actions workflow is provided in .github/workflows/ci.yml to automate testing, model evaluation, and deployment.

## License
This project is licensed under the MIT License.

## Contact
For questions, collaboration, or contributions, please contact dorkhah9@gmail.com