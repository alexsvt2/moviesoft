import os
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_migrate import Migrate  # **

UPLOAD_FOLDER = '/home/alexis/Escritorio/projects/moviesoft/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/alexis/Escritorio/projects/moviesoft/movie_database.db'
db = SQLAlchemy(app)
# ** La aplicacion esta lista para actualizar las tablas en cualquier momento
migrate = Migrate(app, db)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    director = db.Column(db.String(50), unique=False, nullable=False)
    distributor = db.Column(db.String(50), unique=False, nullable=False)
    # Anteriormente existia imagen, pero por estar mal escrito, y confusion se cambio a file
    file = db.Column(db.String(50), unique=False)
    synopsis = db.Column(db.String(500), unique=False, nullable=True)

    def __repr__(self):
        return '<id:%r>' % self.id

@app.route('/', methods=['GET'])
def home():
    # Muestra las portadas en Index
    return render_template('index.html', movies=Movie.query.all())


# @app.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')


# @app.route('/register', methods=['GET'])
# def register():
#     return render_template('register.html')


@app.route('/movies/info/<int:id>', methods=['GET'])
def info(id):
    # Muestra el perfil de una Pelicula seleccionada desde la portada
    movie_info = Movie.query.filter_by(id=id).first()
    if movie_info:
        return render_template('info.html', movie=movie_info)
    return "Ficha de Pelicula no Encontrada"

@app.route('/movies/new_movie', methods=['GET', 'POST'])
def new_movie():
    return render_template('new_movie.html')


def allowed_file(filename):
    """Esta funcion asegura que solamente se cargan archivos de las extensiones permitidas"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/movies', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        category = request.form['category']
        director = request.form['director']
        distributor = request.form['distributor']
        synopsis = request.form['synopsis']
        if not name or not year or not category or not director or not distributor and 'imagen' not in request.files:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('new_movie'))
        if 'file' not in request.files and not name and year:
            flash('All fields required', 'error')
            return redirect(url_for('new_movie'))
        file = request.files['file']
        if file and allowed_file(file.filename):
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            movie = Movie(name=name, year=year, category=category,
                          director=director, distributor=distributor, file=file_name, synopsis=synopsis)
            db.session.add(movie)
            db.session.commit()
        return redirect(url_for('new_movie'))
        # return redirect(url_for('movie'))
    elif request.method == 'GET':
        flash('Welcome', 'error')
        # Esto devuelve el index con la lista de todas las peliculas
        return render_template('show_all.html', movies=Movie.query.all())

@app.route('/movies/<int:id>', methods=['GET'])
def search(id):
    """Se realiza la busqueda de la pelicula utilizando el id en la ruta"""
    # Se tiene que cambiar de nombre la funcion para que coincida con el ingreso a la pelicula en su propio fomulario
    movie_search = Movie.query.filter_by(id=id).first()
    if movie_search:
        return render_template('search.html', movie=movie_search)
    return "No fue encontrada"


@app.route('/movies/delete/<int:id>')
def delete(id):
    """Se realiza la eliminacion de la pelicula utilizando el id en la ruta"""
    movie_delete = Movie.query.filter_by(id=id).first()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], movie_delete.file))
    flash('se ha eliminado una entrada', 'error')
    db.session.delete(movie_delete)
    db.session.commit()
    # flash('se ha eliminado una entrada','error')
    return render_template('show_all.html', movies=Movie.query.all())
    # return redirect(url_for('movie'))

@app.route('/movies/<int:id>', methods=['GET', 'POST'])
def update(id):
    """Actualiza los datos de una pelicula incluida la file"""
    movie_update = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('search.html', movie=movie_update)
    movie_update.name = request.form['name']
    movie_update.year = request.form['year']
    movie_update.category = request.form['category']
    movie_update.director = request.form['director']
    movie_update.distributor = request.form['distributor']
    movie_update.synopsis = request.form['synopsis']
    if 'file' not in request.files:
        # flash('No new Data to Update', 'info')
        movie_update.name = request.form['name']
        movie_update.year = request.form['year']
        movie_update.category = request.form['category']
        movie_update.director = request.form['director']
        movie_update.distributor = request.form['distributor']
        movie_update.synopsis = request.form['synopsis']
        db.session.commit()
        return render_template('search.html', movie=movie_update)
    movie_update_req = request.files['file']
    if not allowed_file(movie_update_req.filename):
        flash('Invalid file type', 'info')
        return render_template('search.html', movie=movie_update)
    if 'file' in request.files and allowed_file(movie_update_req.filename):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], movie_update.file))
        file_name = secure_filename(movie_update_req.filename)
        movie_update.file = file_name
        movie_update_req.save(os.path.join(
            app.config['UPLOAD_FOLDER'], file_name))
    db.session.commit()
    return render_template('search.html', movie=movie_update)


if __name__ == '__main__':
    app.run(debug=True)
