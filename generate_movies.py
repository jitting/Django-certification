import json

movies = []
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Documentary", "Animation", "Adventure"]
years = list(range(1990, 2024))

for i in range(1, 101):
    movie = {
        "title": f"Movie {i}",
        "year": years[i % len(years)],
        "genre": genres[i % len(genres)],
        "director": f"Director {i % 20 + 1}",
        "rating": round(5.0 + (i % 50) / 10, 1),
        "cast": [f"Actor {i}", f"Actor {i + 100}", f"Actor {i + 200}"],
        "plot": f"This is the plot summary for Movie {i}. It's an engaging story about adventure and discovery.",
        "duration": 90 + (i % 60),
        "language": "English"
    }
    movies.append(movie)

with open('movies.json', 'w') as f:
    json.dump(movies, f, indent=2)

print(f"Successfully created movies.json with {len(movies)} movies")
