import pandas as pd

def load_movies(file_path="../data/movies.csv"):
    """
    Load movie metadata from a CSV file.
    Expected columns: movieId, title, genres, description (optional)
    """
    movies = pd.read_csv(file_path)
    # If description column is missing, use title as a placeholder
    if 'description' not in movies.columns:
        movies['description'] = movies['title']
    return movies

def load_ratings(file_path="../data/ratings.csv"):
    """
    Load user ratings from a CSV file.
    Expected columns: userId, movieId, rating, timestamp
    """
    ratings = pd.read_csv(file_path)
    return ratings

def load_reviews(file_path="../data/reviews.csv"):
    """
    Optionally load user reviews for further NLP analysis.
    Expected columns: userId, movieId, review
    """
    try:
        reviews = pd.read_csv(file_path)
        return reviews
    except FileNotFoundError:
        return None

def load_all_data(movies_path="../data/movies.csv", ratings_path="../data/ratings.csv", reviews_path="../data/reviews.csv"):
    """
    Load movies, ratings, and reviews.
    """
    movies = load_movies(movies_path)
    ratings = load_ratings(ratings_path)
    reviews = load_reviews(reviews_path)
    return movies, ratings, reviews
