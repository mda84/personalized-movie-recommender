import pandas as pd

# Define the column names (based on the MovieLens 100k documentation)
columns = ['movieId', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 
           'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 
           'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
           'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('../data/ml-100k/u.item', sep='|', header=None, names=columns, encoding='latin-1')

# Select only the columns we need (movieId, title, release_date)
movies = movies[['movieId', 'title', 'release_date']]

# Create a 'description' column if needed (using the title as a placeholder)
movies['description'] = movies['title']

# Save the DataFrame to CSV in your project's data folder
movies.to_csv('../data/movies.csv', index=False)
print("Movies data saved to data/movies.csv")
