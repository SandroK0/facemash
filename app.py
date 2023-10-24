from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from ranking_algorithm import EloRating
import base64


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    image = db.Column(db.LargeBinary)


@app.route('/', methods=['GET', 'POST'])
def index():

    Images = dict()

    if request.method == "POST":

        winner_id = request.form.get('winner_id')
        looser_id = request.form.get('looser_id')
        winner_rating = request.form.get('winner_rating')
        looser_rating = request.form.get('looser_rating')

        new_winner_rating, new_looser_rating = EloRating(
            int(winner_rating), int(looser_rating))

        winner_image = db.session.query(Image).filter_by(id=winner_id).first()
        winner_image.rating = new_winner_rating
        looser_image = db.session.query(Image).filter_by(id=looser_id).first()
        looser_image.rating = new_looser_rating
        db.session.commit()

    size = db.session.query(Image).count()
    id_1 = randint(1, size)
    id_2 = None
    while True:
        id_2 = randint(1, size)
        if id_2 != id_1:
            break

    image_1 = db.session.query(Image).filter_by(id=id_1).first()
    image_2 = db.session.query(Image).filter_by(id=id_2).first()

    Images["image_1"] = {"id": image_1.id, "rating": image_1.rating,
                         "image": base64.b64encode(image_1.image).decode("utf-8")}
    Images["image_2"] = {"id": image_2.id, "rating": image_2.rating,
                         "image": base64.b64encode(image_2.image).decode("utf-8")}

    return render_template('index.html', images=Images)


@app.route("/leaderboard")
def leaderboard():

    Leaderboard = db.session.query(Image).order_by(Image.rating.desc()).all()

    return render_template("leaderboard.html", Leaderboard=Leaderboard, base64=base64, i=1)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
