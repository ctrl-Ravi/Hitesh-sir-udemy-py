"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""



import os
import json

FILENAME= "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME, 'w', encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

def add_movies(movies):
    title= input("Enter the movie name: ").strip().lower()

    if any(movie["title"].lower()== title for movie in movies):
        print("Movie already exists")
        return
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter Rating (0-10): "))
        if not (0<= rating<=10):
            raise ValueError
    except ValueError:
        print("Please Enter valid number")
        return
    
    movies.append({"title": title, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movies Added ✔️")


def search_movies(movies):
    term = input("Enter the title or genre: ").strip().lower()

    results=[
        movie for movie in movies
        if term in movie['title'].lower() or term in movie['genre'].lower()

     
     ]
    if not results:
        print("No matching result")
        return
    print(f"Found {len(results)} results(s)")

    for movie in results:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']} ")


def view_movies(movies):
    if not movies:
        print("No movies in DB")
        return
    print("__" * 30) 
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']} ")
    print("__" * 30)




def run_movies_db():
    movies = load_movies()

    while True:
        print("\n🍿 My MovieDB")
        print("1. Add movie")
        print("2. View All movies")
        print("3. Search movie")
        print("4. Exit")
    
        choice= input("Choose Your Option Enter (1-4): ").strip()
        match choice:
            case "1" : add_movies(movies)
            case "2" : view_movies(movies)
            case "3" : search_movies(movies)
            case "4" : break
            case _: print("Enter Valid Choice")


if __name__=="__main__": # its only means starting file of python 
    run_movies_db()
    