listaPeliculas = []

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

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")
