from ClassPlaylist import *
import re

mi_playlist = Playlist()
mi_playlist.cargar_playlist()


while True:
    print("------------------------------------------")
    print('''
                Bienvenido a Spotify 
                  Playlist Manager
          ''')
    print("------------------------------------------")
    print("Menú:")
    print("1. Agregar una canción a la playlist")
    print("2. Buscar una canción por su nombre")
    print("3. Filtrar por artista")
    print("4. Reproducir la playlist")
    print("5. Ordenar por número de canción")
    print("6. Ordenar por número de reproducciones")
    print("7. Ordenar por nombre de canción")
    print("8. Mostrar la playlist")
    print("9. Mostrar el historial y conteo de canciones escuchadas")
    print("0. Salir")
    print("-------------------------------------------")

    opcion = input("Ingrese una opción: ")


    if opcion == "1":
        while True:
            try:
                num_cancion = int(input("Ingrese el número de la canción: "))
                if num_cancion >= 16:
                    break
                else:
                    print("El número de la canción debe ser un número entero a partir de 16")
            except ValueError:
                print("El número de la canción debe ser un número entero")

        while True:
            nombre = input("Ingrese el nombre de la canción: ")
            if nombre != "" and re.match("[A-Za-z ]+", nombre):
                break
            else:
                print("El nombre de la canción debe ser una cadena de caracteres alfabéticos y no puede estar vacío")

        while True:
            artista = input("Ingrese el nombre del artista: ")
            if artista != "" and re.match("[A-Za-z ]+", artista):
                break
            else:
                print("El nombre del artista debe ser una cadena de caracteres alfabéticos y no puede estar vacío")

        while True:
            try:
                num_reproduccion = int(input("Ingrese el número de reproducciones: "))
                if num_reproduccion > 0:
                    break
                else:
                    print("El número de reproducciones debe ser un número entero positivo")
            except ValueError:
                print("El número de reproducciones debe ser un número entero")

        while True:
            try:
                año = int(input("Ingrese el año de lanzamiento: "))
                if año > 0:
                    break
                else:
                    print("El año de lanzamiento debe ser un número entero positivo")
            except ValueError:
                print("El año de lanzamiento debe ser un número entero")

        while True:
            idioma = input("Ingrese el idioma de la canción: ")
            if re.match("[A-Za-z]+", idioma):
                break
            else:
                print("El idioma de la canción debe ser una cadena de caracteres alfabéticos")

        mi_playlist.agregar_cancion(num_cancion, nombre, artista, num_reproduccion, año, idioma)



    elif opcion == "2":
        nombre = input("Ingrese el nombre de la canción: ").lower().title()
        if nombre == " ":
            print("El nombre de la canción no puede estar vacío")
        else:
            # La expresión regular [A-Za-z ]+ significa una o más letras de la A a la Z, mayúsculas o minúsculas, o espacios
            if re.match("[A-Za-z ]+", nombre):
                canciones = mi_playlist.buscar_cancion(nombre) # cambiar el nombre de la variable a canciones
                if len(canciones) > 0: # verificar si la lista tiene al menos una canción
                    print("Canciones encontradas:")
                    for cancion in canciones: # hacer un bucle for para mostrar cada canción
                        cancion.mostrar()
                else:
                    print("No se encontró la canción")
            else:
                print("El nombre de la canción no es válido")


    elif opcion == "3":
        artista = input("Ingrese el nombre del artista: ").lower().title()
        if artista == " ":
            print("El nombre del artista no puede estar vacío")
        else:
            if re.match("[A-Za-z ]+", artista):
                canciones_por_artista = mi_playlist.filtrar_por_artista(artista)
                if len(canciones_por_artista) > 0:
                    print("Canciones del artista:")
                    for cancion in canciones_por_artista:
                        cancion.mostrar()
                else:
                    print("No se encontraron canciones del artista")
            else:
                print("El nombre del artista no es válido")

    


    elif opcion == "4":
        while True: 
            print("<><><><><><><><><><><><><")
            print("Menú de reproducciones:")
            print("1. Reproducir playlist")
            print("2. Canción anterior")
            print("3. Siguiente canción")
            print("4. Activar bucle")
            print("5. Desactivar bucle")
            print("6. Salir")
            print("<><><><><><><><><><><><><")
            opcion = input("Elige una opción: ") 
            if opcion == "1": 
                mi_playlist.reproducir() # reproducir la playlist
            elif opcion == "2": 
                mi_playlist.control_reproduccion(0) # reproducir la canción anterior
            elif opcion == "3": 
                mi_playlist.control_reproduccion(1) # reproducir la canción siguiente
            elif opcion == "4":
                mi_playlist.control_reproduccion(2) # activar el modo bucle
            elif opcion == "5": 
                mi_playlist.control_reproduccion(3) # desactivar el modo bucle
            elif opcion == "6": 
                print("Gracias por usar el reproductor de música. Hasta pronto.") 
                break # salir del bucle y terminar el programa
            else: 
                print("Por favor, elige una opción válida.") 
    


    elif opcion == "5":
        while True: 
            print("Orden por número de canción:")
            print("1. Creciente")
            print("2. Decreciente")
            print("3. Salir")
            opcion = input("Elige una opción: ") 
            if opcion == "1": 
                mi_playlist.ordenar_por_numero("creciente") 
            elif opcion == "2": 
                mi_playlist.ordenar_por_numero("decreciente") 
            elif opcion == "3": 
                print("Volver al menú.") 
                break 
            else: 
                print("Por favor, elige una opción válida.") 
    

    elif opcion == "6":
        while True: 
            print("Orden por reproducciones:")
            print("1. Creciente")
            print("2. Decreciente")
            print("3. Salir")
            opcion = input("Elige una opción: ") 
            if opcion == "1": 
                mi_playlist.ordenar_por_reproducciones("creciente") 
            elif opcion == "2": 
                mi_playlist.ordenar_por_reproducciones("decreciente") 
            elif opcion == "3": 
                print("Volver al menú.") 
                break 
            else: 
                print("Por favor, elige una opción válida.") 
    
    
    elif opcion == "7":
        while True: 
            print("Orden por canción:")
            print("1. Creciente")
            print("2. Decreciente")
            print("3. Salir")
            opcion = input("Elige una opción: ") 
            if opcion == "1": 
                mi_playlist.ordenar_por_nombre("creciente") 
            elif opcion == "2": 
                mi_playlist.ordenar_por_nombre("decreciente") 
            elif opcion == "3": 
                print("Volver al menú.") 
                break 
            else: 
                print("Por favor, elige una opción válida.")         
    

    elif opcion == "8":
        mi_playlist.mostrar_playlist()


    elif opcion == "9":
        for nombre, veces in mi_playlist.contar_canciones_historial().items():
            print(f"> {nombre}: {veces}")

    elif opcion == "0":
        print("Hasta la próxima.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")        

















