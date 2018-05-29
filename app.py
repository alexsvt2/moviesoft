from flask import Flask, request, jsonify

database = []

app = Flask(__name__) 

@app.route('/movies', methods=['GET', 'POST'])
def movie():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        category = request.form['category']
        director = request.form['director']
        movie = {"name":name,"year":year,"category":category,"director":director}
        database.append(movie)
        print(movie)
        return jsonify(movie)

    elif request.method == 'GET':
        return jsonify(database)


app.run(debug = True)