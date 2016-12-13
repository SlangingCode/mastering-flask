from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:dragon789@localhost/wfdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Actor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    birthday = db.Column(db.Date())
    deathday = db.Column(db.Date())
    hometown = db.Column(db.String())
    bio = db.Column(db.Text())
    picture = db.Column(db.String())

    def __repr__(self):
        return '<Actor {} {}>'.format(self.first_name, self.last_name)


class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    release_date = db.Column(db.Date())

    def __repr__(self):
        return '<Movie {}>'.format(self.name)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Movie {}>'.format(self.name)


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String)

    def __repr__(self):
        return '<Movie {}>'.format(self.name)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())

    def __repr__(self):
        return '<Comment {}>'.format(self.text[:15])


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()