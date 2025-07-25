import os
os.system('cls')

import Calificaciones

datos = []

def main(): 
    
    opcion=True
    while opcion:
        Calificaciones.borrarPantalla()
        opcion = Calificaciones.menu_principal()    
        match opcion:
            case "1":
                Calificaciones.agregar_calificacion(datos)
                Calificaciones.esperarTecla()
            case "2":
                Calificaciones.mostrar_calificaciones(datos)
                Calificaciones.esperarTecla()
            case "3":
                Calificaciones.calcular_promedio(datos)
                Calificaciones.esperarTecla()
            case "4":
                opcion=False
                print("\n\t\t\t\t\t🎉 Terminaste la ejecucion del programa gracias por usarlo")
                Calificaciones.borrarPantalla()
            case _:
                print("\n\t\t\t\t❌ Opcion invalida, vuelva a intentarlo❌\n")
                Calificaciones.esperarTecla()
                opcion=True

