# funciones.py
def borrarpantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperartecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_principal():
    print(".:: Sistema de Gestión de Notas ::..\n")
    print("1.-  Registro")
    print("2.-  Login")
    print("3.-  Salir")
    opcion = input("\nElige una opción: ").strip().upper()
    return opcion
