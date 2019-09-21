# Guia tecnica

## MovieSoft


## Usuario de la Base de Datos

admin
movie_soft


### Entorno de Desarrollo

El proyecto fue desarrollado utilizando una computadora con estas caracteristicas

```
Ubuntu 18.04 LTS
Memoria: 11.7 GB
Procesador: Intel® Core™ i7-3610QM CPU @ 2.30GHz × 8
Graficos: GeForce GTX 675M/PCIe/SSE2
GNOME: 3.28.1
Tipo de SO: 64 bits
```

Version de **Python** usada en este proyecto
```
Python 3.6.5 (default, Apr  1 2018, 05:46:30)
```

Para poder Instalar el proyecto se requieren las siguientes librerias, se incluye un archivo llamado **requirements.txt** donde se explica como instalar las librerias con pip install

```
alembic==0.9.9  
backcall==0.1.0  
click==6.7  
decorator==4.3.0  
Flask==1.0.2  
Flask-Migrate==2.2.1  
Flask-Modus==0.0.1  
Flask-Script==2.0.6  
Flask-SQLAlchemy==2.3.2  
ipython==6.4.0  
ipython-genutils==0.2.0  
itsdangerous==0.24  
jedi==0.12.0  
Jinja2==2.10  
Mako==1.0.7  
MarkupSafe==1.0  
parso==0.2.1  
pexpect==4.6.0  
pickleshare==0.7.4  
prompt-toolkit==1.0.15  
psycopg2==2.7.4  
ptyprocess==0.5.2  
Pygments==2.2.0  
python-dateutil==2.7.3  
python-editor==1.0.3  
simplegeneric==0.8.1  
six==1.11.0  
SQLAlchemy==1.2.8  
traitlets==4.3.2  
wcwidth==0.1.7  
Werkzeug==0.14.1  
```

### Levantar el Proyecto

Para levantar el proyecto se requieren seguir estos pasos:

- Usar virtualenv
- Descargar el repositorio de github
- iniciar la aplicacion con python app.py

#### Instalacion

Se debe corregir la carpeta de statics donde van los archivos de carga, solo para que coincidan con los datos locales, y la ruta donde se guarda la base de datos, mas adelante corregire todos los errores de Moviesoft.

Se recomienda que el usuario cree una carpeta donde va a realizar git clone, por ejemplo **projects**

```
$ git clone https://github.com/alexsvt2/moviesoft.git
```

Si el usuario realiza git clone dentro de proyects, el proyecto se veria asi
```
projects/moviesoft
```
Dentro de projects inicia una terminal y corre los siguientes comandos para activar el entorno virtual
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Cuando el virtualenv este trabajando deberias poder ver (venv) y entonces es momento de realizar la instalacion de las librerias necesarias
```
(venv) ➜  projects
```

```
# Abre una termina dentro de moviesoft
# projects/moviesoft/
```
y escribe los siguientes comandos

```
$ pip install -r requirements.txt
# Entonces comenzara a configurarse todo lo necesario para que la aplicacion corra
```

#### Ejecutar

Con el virtualenv activado abre una terminal dentro de projects/moviesoft y escribe

```
python3 app.py
```

Para entrar a la aplicacion de manera local se puede ingresar de dos maneras, usando el http://localhost:5000/ o http://127.0.0.1:5000/


#### Endpoints

<table style="undefined;table-layout: fixed; width: 774px">
  <tr>
    <th>Metodo HTTP</th>
    <th>URI</th>
    <th>OPERACION</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/</td>
    <td>Muestra las portadas en la pantalla principal de la aplicacion</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/movies/info/1<br></td>
    <td>Muestra la informacion de la pelicula con el id 1</td>
  </tr>
  <tr>
    <td>GET, POST</td>
    <td>/movies/new_movie<br></td>
    <td>Muestra el formulario de nueva pelicula</td>
  </tr>
  <tr>
    <td>GET, POST</td>
    <td>/movies</td>
    <td>Muestra la lista de peliculas, junto con la accion borrar</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/movies/2</td>
    <td>Permite acceder a la pelicula con id 2 desde la lista de peliculas en /movies</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>/movies/delete/3<br></td>
    <td>Realiza el borrado de la pelicula con id 3</td>
  </tr>
  <tr>
    <td>GET, POST</td>
    <td>/movies/1</td>
    <td>Permite actualizar los datos de la pelicula 1</td>
  </tr>
</table>

### Base de Datos y Migraciones

Una parte importante de la aplicacion es poder crear nuevos modelos y actualizarlos, actualmente todo se encuentra en el mismo archivo, sin embargo voy a empezar a cambiar de lugares los scripts para poder limpiar el app principal

de Momento es importante saber que la creacion de la base de datos se realiza 
En el folder raiz del project

Se ejecuta el interprete de Python en la consola

```
python
#
>>> from app import db
>>> db.create_all()
```
La ejecucion de estas lineas provocara que si la base de datos no existe, sea creada

Para ejecutar las migraciones(Cuando se modifica la estructura de la base de datos)
Adjunto una url para consultar las migraciones
https://flask-migrate.readthedocs.io/en/latest/