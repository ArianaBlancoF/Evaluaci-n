from ClassCancion import *
import random

class Playlist():
    def __init__(self):
        self.canciones = []
        self.indice_actual = 0 
        self.bucle = False 
        self.reproducciones = 0
        self.historial = []



    def cargar_playlist(self):
        try:
            with open('Playlist.txt', 'r') as f:
                archivo = f.readlines() 
            for linea in archivo:
                datos = linea.strip().split(",")
                cancion = Cancion(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
                self.canciones.append(cancion)
        except IOError:
            print("No se pudo abrir o leer el archivo")




    def agregar_cancion(self, num_cancion, nombre, artista, num_reproduccion, año, idioma):
        cancion = Cancion(num_cancion, nombre, artista, num_reproduccion, año, idioma)
        self.canciones.append(cancion)
        with open('Playlist.txt', 'w') as f:
            for cancion in self.canciones:
                f.write(f"{cancion.num_cancion},{cancion.nombre},{cancion.artista},{cancion.num_reproduccion},{cancion.año},{cancion.idioma}\n")
        print("Nueva canción agregada con éxito")




    def buscar_cancion(self, nombre):
        canciones_nombre = []
        for cancion in self.canciones:
            if cancion.nombre.upper().strip().startswith(nombre.upper().strip()):
                canciones_nombre.append(cancion)
        return canciones_nombre



    def filtrar_por_artista(self, artista):
        canciones_artista = []
        for cancion in self.canciones:
            if cancion.artista.upper().strip().startswith(artista.upper().strip()): 
                canciones_artista.append(cancion)
        return canciones_artista




    def reproducir_cancion(self):
        cancion = self.canciones[self.indice_actual]
        print(f"Reproduciendo: {cancion.nombre} - {cancion.artista}")
        self.indice_actual += 1
        self.historial.append(cancion) 

    def reproducir(self):
        self.reproduciendo = True # activar la reproducción
        if self.indice_actual >= len(self.canciones): 
            print("Fin de la reproducción.") 
            self.reproduciendo = False 
            if self.bucle: 
                random.shuffle(self.canciones) 
                self.reproducciones += 1 # incrementar el contador de reproducciones
                print(f"Se ha reproducido la playlist {self.reproducciones} veces. Empezando de nuevo...") 
                self.indice_actual = 0 # volver al principio de la lista        
        else: 
            if self.bucle: # si el modo bucle está activado
                random.shuffle(self.canciones) # mezcla la lista de canciones
                print("Mezclando canciones...")         
            self.reproducir_cancion() # reproducir la canción actual

    def control_reproduccion(self, accion):
        if accion == 0: # Canción anterior    ////////  ESTA ACCIÓN NO CORRE BIEN ////// === 
            if self.indice_actual > 0: 
                self.indice_actual -= 1
                self.reproducir() 
            else:
                print("No hay ninguna canción anterior por el momento.")
        elif accion == 1: # Canción siguiente    //////////   ESTA TAMPOCO CORRE BIEN ///////====
            if self.indice_actual < len(self.canciones) - 1: 
                self.indice_actual += 1
                self.reproducir() 
            else: 
                self.indice_actual = 0
                print("La última canción de la lista ya se está reproduciendo.")
        elif accion == 2: # Bucle
            self.bucle = True 
            print("Se ha activado el modo bucle.") 
        elif accion == 3: # Eliminar Bucle
            if self.bucle: 
                self.bucle = False 
                print("Se ha desactivado el modo bucle.") 
            else:
                print("El modo bucle no está activado.") 






    def contar_canciones_historial(self):
        conteo = {} # Diccionario vacío para almacenar el conteo de canciones
        for cancion in self.historial:
            if cancion.nombre in conteo:
                conteo[cancion.nombre] += 1
            else:
                conteo[cancion.nombre] = 1
        return conteo




    def mostrar_playlist(self):
        for cancion in self.canciones:
            cancion.mostrar()
            print()




    def burbuja_creciente_numero(self):
        n = len(self.canciones)
        intercambiado = True # inicializar la variable intercambiado a True
        while intercambiado: # mientras haya algún intercambio
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].num_cancion > self.canciones[j + 1].num_cancion: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True # marcar que se ha hecho un intercambio
            n -= 1 # reducir el tamaño de la lista a ordenar en uno

    def burbuja_decreciente_numero(self):
        n = len(self.canciones)
        intercambiado = True 
        while intercambiado: 
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].num_cancion < self.canciones[j + 1].num_cancion: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True 
            n -= 1 

    def ordenar_por_numero(self, orden):
        if orden == "creciente" : 
            self.burbuja_creciente_numero()
            self.mostrar_playlist() 
        elif orden == "decreciente": 
            self.burbuja_decreciente_numero()
            self.mostrar_playlist()
        else: 
            print("Orden inválido") 





    def burbuja_creciente_reproducciones(self):
        n = len(self.canciones)
        intercambiado = True 
        while intercambiado: 
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].num_reproduccion > self.canciones[j + 1].num_reproduccion: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True 
            n -= 1 

    def burbuja_decreciente_reproducciones(self):
        n = len(self.canciones)
        intercambiado = True 
        while intercambiado: 
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].num_reproduccion < self.canciones[j + 1].num_reproduccion: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True 
            n -= 1 

    def ordenar_por_reproducciones(self, orden):
        if orden == "creciente" : 
            self.burbuja_creciente_reproducciones()
            self.mostrar_playlist() 
        elif orden == "decreciente": 
            self.burbuja_decreciente_reproducciones()
            self.mostrar_playlist() 
        else: 
            print("Orden inválido") 




    
    
    def burbuja_creciente_nombre(self):
        n = len(self.canciones)
        intercambiado = True 
        while intercambiado: 
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].nombre > self.canciones[j + 1].nombre: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True 
            n -= 1 

    def burbuja_decreciente_nombre(self):
        n = len(self.canciones)
        intercambiado = True 
        while intercambiado: 
            intercambiado = False 
            for j in range(0, n-1): 
                if self.canciones[j].nombre < self.canciones[j + 1].nombre: 
                    self.canciones[j], self.canciones[j + 1] = self.canciones[j + 1], self.canciones[j] 
                    intercambiado = True 
            n -= 1 

    def ordenar_por_nombre(self, orden):
        if orden == "creciente": 
            self.burbuja_creciente_nombre()
            self.mostrar_playlist() 
        elif orden == "decreciente": 
            self.burbuja_decreciente_nombre()
            self.mostrar_playlist() 
        else:
            print("Orden inválido") 













