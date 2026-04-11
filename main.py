from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, Zhaina!"}


@app.get("/greet")
def greet(name: str = "Student Zhaina"):
    return {"greeting": f"Hello, {name}!"}



movies = [
    {"title": "Inception", "year": 2010},
    {"title": "Interstellar", "year": 2014},
    {"title": "The Dark Knight", "year": 2008}
]

@app.get("/movies")
def get_movies():
    return {"movies": movies}
@app.get("/movies/filter")
def filter_movies(year: int = 2000):
    filtered = [m for m in movies if m["year"] >= year]
    return {"filtered_movies": filtered}



