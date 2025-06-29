'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menu de opciones para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar listas para almacenar los nombres de peliculas
'''
import peliculas

opcion = True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::GESTION DE PELICULAS:::.\n\t1.-Agregar Peliculas \n\t2.-Borrar Peliculas \n\t3.-Modificar Peliculas Agregadas" \
    "\n\t4.-Mostrar Peliculas\n\t5.-Buscar Peliculas\n\t6.-Limpiar Peliculas Agregadas\n\t7.-Salir del Sistema")
    opcion = input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()

        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()

        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()

        case "4":
            if not peliculas.listaPeliculas:
                print("\n\tNo hay películas para mostrar.")
            else:
                print("\n\tListado de las primeras 4 películas:\n")
                for i, pelicula in enumerate(peliculas.listaPeliculas[:4], start=1):
                    print(f"\t{i}. {pelicula}")
            peliculas.esperarTecla()

        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()

        case "6":
            confirmar = input("\n\t¿Quieres limpiar la lista de películas? (S/N): ").upper()
            if confirmar == "S":
                peliculas.listaPeliculas.clear()
                print("\n\tLista de películas vaciada correctamente.")
            else:
                print("\n\tOperación cancelada.")
            peliculas.esperarTecla()

        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")

        case _:
            print("\n\tOpción Inválida, vuelva a intentarlo")
            peliculas.esperarTecla()

