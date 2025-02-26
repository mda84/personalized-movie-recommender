import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def collaborative_filtering_recommendations(user_id, movies, ratings, top_n=10):
    """
    Generate recommendations using collaborative filtering (matrix factorization).
    """
    # Create a user-item matrix; missing ratings are filled with 0.
    user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    
    # Apply dimensionality reduction using TruncatedSVD.
    svd = TruncatedSVD(n_components=20, random_state=42)
    latent_matrix = svd.fit_transform(user_item_matrix)
    reconstructed = np.dot(latent_matrix, svd.components_)
    predicted_ratings = pd.DataFrame(reconstructed, index=user_item_matrix.index, columns=user_item_matrix.columns)
    
    # Identify movies that the user has not yet rated.
    user_rated = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    user_predictions = predicted_ratings.loc[user_id].drop(labels=user_rated)
    
    # Get top_n movie IDs based on predicted ratings.
    recommended_movie_ids = user_predictions.sort_values(ascending=False).head(top_n).index.tolist()
    
    # Return movie titles from the movies dataframe.
    recommendations = movies[movies['movieId'].isin(recommended_movie_ids)]
    return recommendations[['movieId', 'title']]

def content_based_recommendations(movie_id, movies, top_n=10):
    """
    Generate recommendations using content-based filtering on movie descriptions.
    """
    movies['description'] = movies['description'].astype(str)
    
    # Compute TF-IDF vectors for movie descriptions.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['description'])
    
    # Compute cosine similarity between movies.
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get the index corresponding to the input movie_id.
    indices = pd.Series(movies.index, index=movies['movieId']).drop_duplicates()
    idx = indices.get(movie_id, None)
    if idx is None:
        return pd.DataFrame()  # Movie not found
    
    # Get similarity scores and select the top_n similar movies (excluding the movie itself).
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_indices = [i[0] for i in sim_scores[1:top_n+1]]
    
    recommendations = movies.iloc[sim_indices]
    return recommendations[['movieId', 'title']]

def hybrid_recommendations(user_id, movies, ratings, top_n=10, weight_cf=0.5, weight_cb=0.5):
    """
    Generate recommendations using a hybrid approach that combines collaborative filtering
    and content-based filtering.
    """
    # Get CF recommendations.
    cf_recs = collaborative_filtering_recommendations(user_id, movies, ratings, top_n=top_n*2)
    cf_recs = cf_recs.copy()
    cf_recs['cf_score'] = 1.0  # For simplicity, assign a uniform score.
    
    # For content-based, select the user's favorite movie (highest rated).
    user_ratings = ratings[ratings['userId'] == user_id]
    if user_ratings.empty:
        hybrid = cf_recs.copy()
        hybrid['hybrid_score'] = hybrid['cf_score']
        return hybrid[['movieId', 'title']]
    
    favorite_movie_id = user_ratings.sort_values(by='rating', ascending=False)['movieId'].iloc[0]
    cb_recs = content_based_recommendations(favorite_movie_id, movies, top_n=top_n*2)
    cb_recs = cb_recs.copy()
    cb_recs['cb_score'] = 1.0  # Assign a uniform score.
    
    # Merge and combine scores.
    combined = pd.merge(cf_recs, cb_recs, on=['movieId', 'title'], how='outer')
    combined['cf_score'] = combined['cf_score'].fillna(0)
    combined['cb_score'] = combined['cb_score'].fillna(0)
    combined['hybrid_score'] = weight_cf * combined['cf_score'] + weight_cb * combined['cb_score']
    combined = combined.sort_values(by='hybrid_score', ascending=False)
    
    return combined[['movieId', 'title']].head(top_n)

def get_recommendations(user_id, movies, ratings, method='hybrid', top_n=10):
    """
    Main function to retrieve recommendations based on the specified method.
    Methods available: 'collaborative', 'content', or 'hybrid'.
    """
    if method == 'collaborative':
        return collaborative_filtering_recommendations(user_id, movies, ratings, top_n)
    elif method == 'content':
        user_ratings = ratings[ratings['userId'] == user_id]
        if user_ratings.empty:
            return pd.DataFrame()
        favorite_movie_id = user_ratings.sort_values(by='rating', ascending=False)['movieId'].iloc[0]
        return content_based_recommendations(favorite_movie_id, movies, top_n)
    elif method == 'hybrid':
        return hybrid_recommendations(user_id, movies, ratings, top_n)
    else:
        raise ValueError("Invalid method. Choose 'collaborative', 'content', or 'hybrid'.")
