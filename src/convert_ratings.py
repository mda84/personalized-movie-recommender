import pandas as pd

# Load the ratings data; columns are user id, item id, rating, and timestamp
ratings = pd.read_csv('../data/ml-100k/u.data', sep='\t', header=None, names=['userId', 'movieId', 'rating', 'timestamp'])

# Optionally, drop the timestamp if not needed
ratings = ratings.drop(columns=['timestamp'])

# Save the DataFrame to CSV in your project's data folder
ratings.to_csv('../data/ratings.csv', index=False)
print("Ratings data saved to data/ratings.csv")
