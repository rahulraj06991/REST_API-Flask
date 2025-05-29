# REST_API-Flask
This is a RESTful API built using Python, Flask, and SQLAlchemy for managing movie information. It supports CRUD operations (Create, Read, Update, Delete) and allows users to store and retrieve movie details such as name, genre, and rating.

Features

- GET /movies: Retrieve all stored movies
- GET /movie/<id>: Get a specific movie by ID
- POST /movies: Add a new movie (requires JSON body)
- PUT /movies/<id>: Update details of a specific movie
- DELETE /movies/<id>: Delete a movie by ID

Tech Stack
- Python
- Flask – Web framework
- SQLAlchemy – ORM for database operations

Data Model

{
    "movie_name": "Dangal",
    "rating": 9.5,
    "genre": "Sports, Drama"
}

Setup and Run
- pip install -r requirements.txt
- python main.py
