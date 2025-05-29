from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String[50], nullable=False)
    genre = db.Column(db.String[50], nullable=False)
    rating = db.Column(db.Float, nullable= False)

    def to_dict(self):
        return {
            "id": self.id,
            "movie_name": self.movie_name,
            "genre": self.genre,
            "rating": self.rating
        }

with app.app_context():
    db.create_all()


#routes
@app.route("/")
def home():
    return jsonify({"message":"This an API to find best movies"})

#get
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

#get a particular movie
@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        return jsonify(movie.to_dict())
    else:
        return jsonify({"error": "destination not found"})

#post movies    
@app.route("/movies", methods=["POST"])
def add_movies():
    data = request.get_json()

    new_movies = Movie(movie_name= data["movie_name"],
                                  genre = data["genre"],
                                  rating = data['rating'])
    
    db.session.add(new_movies)
    db.session.commit()
    return jsonify(new_movies.to_dict()), 201

#put (update movie)
@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()

    movie = Movie.query.get(movie_id)
    if movie:
        movie.movie_name = data.get("movie_name", movie.movie_name)
        movie.genre = data.get("genre", movie.genre)
        movie.rating = data.get("rating", movie.rating)

        db.session.commit()

        return jsonify(movie.to_dict())
    else:
        return jsonify({"error": "Movie not found"}), 404
    
#delete movies
@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):  
    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"message": "Movie deleted"}) 
    else:
        return jsonify({"error":"Movie not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)