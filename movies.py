class Movies():
    def __init__(self, *args):
        self.name = args
        self.year = args
        self.category = args
        self.director = args

    def mostrar_informacion(self):
        print(self.name, self.year, self. category, self.director)


mi_pelicula = Movies('Alien', 1979, 'Terror', 'Ridley Scott')
mi_pelicula.mostrar_informacion()


