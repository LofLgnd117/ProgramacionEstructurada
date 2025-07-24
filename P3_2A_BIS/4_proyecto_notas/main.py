# MAIN.py
import funciones
import usuario
import nota

def main():
    opcion = True
    while opcion:
        funciones.borrarpantalla()
        seleccion = funciones.menu_principal()

        if seleccion == "1" or seleccion == "REGISTRO":
            usuario.registrar_usuario()
        elif seleccion == "2" or seleccion == "LOGIN":
            if usuario.login():
                nota.menu_notas()
        elif seleccion == "3" or seleccion == "SALIR":
            print("\n\tTermino la Ejecución del Sistema")
            opcion = False
            funciones.esperartecla()
        else:
            print("\n\tOpcion no válida")
            funciones.esperartecla()

if __name__ == "__main__":
    main()
