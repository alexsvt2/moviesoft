# from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/alexis/Escritorio/projects/moviesoft/movie_database.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    director = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<ID %r>' % self.id

# pelicula1 = Movie(name='Alien', year=1979, category='Terror', director='Ridley Scott')
# pelicula2 = Movie(name='Transformers', year=2007, category='Ficcion', director='Michael Bay')

# db.create_all()
# db.session.add(pelicula1)
# db.session.add(pelicula2)
# db.session.commit()