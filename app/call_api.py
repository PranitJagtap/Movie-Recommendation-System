import requests

def call_genre(data):
    local = "http://127.0.0.1:8000/recommend_movies_content"
    movies = requests.post(local, json=data)
    return movies.text
