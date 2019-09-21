"""Este archivo es el generador de la base de datos, SIEMPRE SE DEBE TENER EN CUENTA LA RUTA DE LA CREATION DE LA BASE DE DATOS"""

# from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviesoft/test_db.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    # year = db.Column(db.Date, unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    director = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<ID %r>' % self.id