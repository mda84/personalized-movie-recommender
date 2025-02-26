import pandas as pd

# Create a dummy reviews DataFrame
dummy_reviews = pd.DataFrame({
    'userId': [1, 1, 2, 2, 3],
    'movieId': [1, 2, 1, 3, 2],
    'review': [
        "Great movie, loved the story!",
        "Not my cup of tea.",
        "Fantastic visuals and plot.",
        "Mediocre performance, could be better.",
        "A true masterpiece!"
    ]
})

# Save the dummy reviews to CSV
dummy_reviews.to_csv('../data/reviews.csv', index=False)
print("Dummy reviews saved to data/reviews.csv")
