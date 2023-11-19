from ClassCancion import *
import random

class Playlist():
    def __init__(self):
        self.canciones = []
        self.indice_actual = 0 
        self.bucle = False 



    def cargar_playlist(self):
        with open('Playlist.txt', 'r') as f:
            archivo = f.readline()
            for linea in archivo:
                datos = linea.strip().split(",")
                cancion = Cancion(int(datos[0]), datos[1], int(datos[2]), int(datos[3]), datos[4])
                self.canciones.append(cancion)
    


    def agregar_cancion(self, num_cancion, nombre, artista, num_reproduccion, año, idioma):    #DUDAS_REVISAR/////
        cancion = Cancion(num_cancion, nombre, artista, num_reproduccion, año, idioma)
        self.canciones.append(cancion)



    def buscar_cancion(self, nombre):
        for cancion in self.canciones:
            if cancion.nombre == nombre:
                return cancion
        return None



    def filtrar_por_artista(self, artista):
        canciones_artista = []
        for cancion in self.canciones:
            if cancion.artista == artista:
                canciones_artista.append(cancion)
        return canciones_artista



    def reproducir_cancion(self):
        cancion = self.canciones[self.indice_actual]
        print(f"Reproduciendo: {cancion.nombre} - {cancion.artista}")
        self.indice_actual += 1

    def reproducir(self):
        while True:
            if self.bucle:
                if self.indice_actual >= len(self.canciones):
                    self.indice_actual = 0
                    random.shuffle(self.canciones) # mezcla la lista de canciones
                    print("Se ha reproducido toda la playlist. Mezclando canciones...")
                self.reproducir_cancion()
            else:
                if self.indice_actual >= len(self.canciones):
                    print("Fin de la reproducción.")
                    break
                self.reproducir_cancion()

    def control_reproduccion(self, accion):
        if accion == 0: # Canción anterior
            if self.indice_actual > 0:
                self.indice_actual -= 1
        elif accion == 1: # Canción siguiente
            if self.indice_actual < len(self.canciones) - 1:
                self.indice_actual += 1
        elif accion == 2: # Bucle
            self.bucle = True
        elif accion == 3: # Eliminar Bucle
            self.bucle = False



    def mostrar_playlist(self):
        for cancion in self.canciones:
            cancion.mostrar()
            print()












