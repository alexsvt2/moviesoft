from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/alexis/Escritorio/projects/moviesoft/movie_database.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    director = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return '<id:%r>' % self.id
    
    # def __init__(self, name, year, category, director):
    #     self.name = name
    #     self.year = year
    #     self.category = category
    #     self.director = director


@app.route('/movies', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        category = request.form['category']
        director = request.form['director']
        movie = Movie(name=name, year=year, category=category, director=director)
        db.session.add(movie)
        db.session.commit()        
        return "Se ha creado una pelicula"
    elif request.method == 'GET':
        return render_template('index.html', movies=Movie.query.all()) # Esto devuelve el index con la lista de todas las peliculas

@app.route('/movies/<int:id>', methods=['GET'])
def search(id):
    """Se realiza la busqueda de la pelicula utilizando el id en la ruta"""
    movie_search = Movie.query.filter_by(id=id).first()
    if movie_search:
        return render_template('search.html', movie=movie_search)    
    return "No encontrado"

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete(id):
    """Se realiza la eliminacion de la pelicula utilizando el id en la ruta"""
    movie_delete = Movie.query.filter_by(id=id).first()
    if request.method == 'DELETE':
        db.session.delete(movie_delete)
        db.session.commit()
        return "Se ha eliminado de la base de Datos"

# @app.route('/movies/<int:movie_id>', methods=['PUT'])
# def update(movie_id):
#     if request.method == 'PUT':
#         movie_update = list(filter(lambda x: x['id'] == movie_id, database))
#         if request.form['name'] != '':
#             movie_update[0]['name'] = request.form['name']
#         if request.form['year'] != '':
#             movie_update[0]['year'] = request.form['year']
#         if request.form['category'] != '':
#             movie_update[0]['category'] = request.form['category']
#         if request.form['director'] != '':
#             movie_update[0]['director'] = request.form['director']
#         database.append(movie_update)
#     return jsonify(database)

if __name__=='__main__':
    app.run(debug = True)