
class Cancion:
    def __init__(self,num_cancion, nombre, artista, num_reproduccion, año, idioma):
        self.num_cancion = num_cancion        
        self.nombre = nombre
        self.artista = artista
        self.num_reproduccion = num_reproduccion
        self.año = año
        self.idioma = idioma

    def mostrar(self):
        """
        Muestra información sobre las canciones.
        """
        print(f"> Nombre de la canción: {self.nombre}")
        print(f"> Nombre del artista: {self.artista}")
        print(f"> Número de reproducciones: {self.num_reproduccion}") 
        print(f"> Año: {self.año}")
        print(f"> Idioma: {self.idioma}")
