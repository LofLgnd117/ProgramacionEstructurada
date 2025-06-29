listaPeliculas = []
'''
def agregarPeliculas():
    nombre = input("Ingresa el nombre de la película: ")
    listaPeliculas.append(nombre)
    print(f"{nombre} fue agregada a la lista de películas.")

def borrarPeliculas():
    if not listaPeliculas:
        print("No hay películas para borrar.")
        return

    mostrarPeliculas()
    try:
        idx = int(input("Ingresa el número de la película a borrar: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            borrada = listaPeliculas.pop(idx)
            print(F"{borrada} fue eliminada con exito")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        
def modificarPeliculas():
    print("..:::MODIFICAR PELICULAS:::.")
    if not listaPeliculas:
        print("No hay películas para modificar.")
        return
    nombre = input("Ingresa el nombre de la película a modificar: ")
    if nombre in listaPeliculas:
        nuevo = input("Ingresa el nuevo nombre: ")
        index = listaPeliculas.index(nombre)
        listaPeliculas[index] = nuevo
        print("Película modificada.")
    else:
        print("Película no encontrada.")

def mostrarPeliculas():
    for i, pelicula in enumerate(listaPeliculas, start=1):
        print(f"{i}. {pelicula}")

def buscarPeliculas():
    nombre = input("Ingresa el nombre a buscar: ")
    encontrados = [p for p in listaPeliculas if nombre.lower() in p.lower()]
    if encontrados:
        print("Películas encontradas:")
        for p in encontrados:
            print(f"- {p}")
    else:
        print("No se encontraron coincidencias.")
'''
def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

#Diccionaro u objeto para almacenar los siguientes atributos de las peliculas: nombre, categoria, clasificacion, genero, idioma
def agregarPeliculas():
    pelicula = {}
    pelicula['nombre'] = input("Ingresa el nombre de la película: ")
    pelicula['categoria'] = input("Ingresa la categoría de la película: ")
    pelicula['clasificacion'] = input("Ingresa la clasificación de la película: ")
    pelicula['genero'] = input("Ingresa el género de la película: ")
    pelicula['idioma'] = input("Ingresa el idioma de la película: ")
    
    listaPeliculas.append(pelicula)
    print(f"{pelicula['nombre']} fue agregada a la lista de películas.")

def crearPelicula():
    pelicula = {
        'nombre': input("Ingresa el nombre de la película: "),
        'categoria': input("Ingresa la categoría de la película: "),
        'clasificacion': input("Ingresa la clasificación de la película: "),
        'genero': input("Ingresa el género de la película: "),
        'idioma': input("Ingresa el idioma de la película: ")
    }
    listaPeliculas.append(pelicula)
    print(f"{pelicula['nombre']} fue agregada a la lista de películas.")

def mostrarpeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::MOSTRAR PELICULAS:::.")
    if not listaPeliculas:
        print("No hay películas para mostrar.")
        return

    for i, pelicula in enumerate(listaPeliculas, start=1):
        print(f"{i}. Nombre: {pelicula['nombre']}, Categoría: {pelicula['categoria']}, "
              f"Clasificación: {pelicula['clasificacion']}, Género: {pelicula['genero']}, Idioma: {pelicula['idioma']}")
        
def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::BORRAR PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para borrar.")
        return

    mostrarpeliculas()
    try:
        idx = int(input("Ingresa el número de la película a borrar: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            borrada = listaPeliculas.pop(idx)
            print(f"{borrada['nombre']} fue eliminada con éxito.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::MODIFICAR PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para modificar.")
        return

    mostrarpeliculas()
    try:
        idx = int(input("Ingresa el número de la película a modificar: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            pelicula = listaPeliculas[idx]
            print(f"Modificando {pelicula['nombre']}")
            pelicula['nombre'] = input("Nuevo nombre: ")
            pelicula['categoria'] = input("Nueva categoría: ")
            pelicula['clasificacion'] = input("Nueva clasificación: ")
            pelicula['genero'] = input("Nuevo género: ")
            pelicula['idioma'] = input("Nuevo idioma: ")
            print(f"{pelicula['nombre']} fue modificada con éxito.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::AGREGAR CARACTERISTICA PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para agregar características.")
        return

    mostrarpeliculas()
    try:
        idx = int(input("Ingresa el número de la película a la que deseas agregar una característica: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            pelicula = listaPeliculas[idx]
            caracteristica = input("Ingresa la característica a agregar: ")
            pelicula['caracteristica'] = caracteristica
            print(f"Característica '{caracteristica}' agregada a {pelicula['nombre']}.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::BORRAR CARACTERISTICA PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para borrar características.")
        return

    mostrarpeliculas()
    try:
        idx = int(input("Ingresa el número de la película de la que deseas borrar una característica: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            pelicula = listaPeliculas[idx]
            if 'caracteristica' in pelicula:
                del pelicula['caracteristica']
                print(f"Característica borrada de {pelicula['nombre']}.")
            else:
                print(f"{pelicula['nombre']} no tiene características para borrar.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ser un número.")