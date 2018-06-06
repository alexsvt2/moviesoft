from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
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

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html')
    
@app.route('/movies', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        category = request.form['category']
        director = request.form['director']
        if not name or not year or not category or not director:
            flash('Introduce todos los datos requeridos')
            # return 'Introduce todos los campos'
        movie = Movie(name=name, year=year, category=category, director=director) #Instancia
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('movie'))
    elif request.method == 'GET':
        return render_template('movieindex.html', movies=Movie.query.all()) # Esto devuelve el index con la lista de todas las peliculas

@app.route('/movies/<int:id>', methods=['GET'])
def search(id):
    """Se realiza la busqueda de la pelicula utilizando el id en la ruta"""
    movie_search = Movie.query.filter_by(id=id).first()
    if movie_search:
        return render_template('search.html', movie=movie_search)    
    return "No fue encontrada"

@app.route('/movies/delete/<int:id>')
def delete(id):
    """Se realiza la eliminacion de la pelicula utilizando el id en la ruta"""
    movie_delete = Movie.query.filter_by(id=id).first()
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for('movie'))

@app.route('/movies/<int:id>', methods=['GET', 'POST'])
def update(id):
    """Actualiza los datos de una pelicula"""
    movie_update = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('search.html', movie=movie_update)
    movie_update.name = request.form['name']
    movie_update.year = request.form['year']
    movie_update.category = request.form['category']
    movie_update.director = request.form['director']
    db.session.commit()
    # return redirect(url_for('movie'))
    # return redirect(url_for('movie'))
    return render_template('search.html', movie=movie_update)
    

if __name__=='__main__':
    app.run(debug = True)