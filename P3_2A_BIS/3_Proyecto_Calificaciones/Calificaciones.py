SISTEMA# Calificaciones.py (integrado con MySQL)
import os
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

def menu_principal():
    print("\t\t\t\t 📜 .::: SISTEMA DE CALIFICACIONES :::. 📜\n")
    print("\t\t\t\t	 1️⃣  ➔  Agregar")
    print("\t\t\t\t	 2️⃣  ➔  Mostrar")
    print("\t\t\t\t	 3️⃣  ➔  Calcular Promedio")
    print("\t\t\t\t	 4️⃣  ➔  Salir\n")
    opcion = input("\t\t\t\t🔍 Selecciona una opción de 1-4: ").strip()
    return opcion

def agregar_calificacion():
    borrarPantalla()
    print("\t\t\t\t📂 .::AGREGAR CALIFICACIONES::. 📂\n")
    nombre = input("\t\t\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"\n\t\t\t📝 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("\n\t\t\t\t❌ Ingrese un número válido entre 0 y 10 ❌\n")
            except ValueError:
                print("\n\t\t\t\t❌ Ingrese un valor numérico ❌\n")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO calificaciones (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)",
                           (nombre, calificaciones[0], calificaciones[1], calificaciones[2]))
            conexion.commit()
            print("\n\t\t\t\t🎉 Acción realizada con éxito 🎉\n")
        except Error as e:
            print(f"\n\t\t\t\t❌ Error al guardar: {e}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_calificaciones():
    ancho = 115
    borrarPantalla()
    print("\t\t\t\t📂 .::MOSTRAR CALIFICACIONES::. 📂\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"\t\t\t\t{'::Nombre::':<15}{'::Calif1::':<12}{'Calif2::':<12}{'::Calif3::':<12}")
            print(("-" * 60).center(ancho))
            for fila in registros:
                print(f"\t\t\t\t{fila[0]:<15}{fila[1]:<12}{fila[2]:<12}{fila[3]:<12}")
            print(("-" * 60).center(ancho))
            print(f"\n\t\t\t\t Son {len(registros)} alumnos\n")
        else:
            print("\t\t\t\t⚠  No hay calificaciones registradas.\n")
        cursor.close()
        conexion.close()

def calcular_promedio():
    borrarPantalla()
    ancho = 90
    print("\t\t\t\t📂 .::PROMEDIO DE ALUMNOS::. 📂\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"\t\t\t\t{'::Nombre::':<15}{'::Promedio::':<12}")
            print(("-" * 32).center(ancho))
            promedio_grupal = 0
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                print(f"\t\t\t\t{fila[0]:<15}{promedio:<12.2f}")
                promedio_grupal += promedio
            promedio_grupal /= len(registros)
            print(("-" * 32).center(ancho))
            print(f"\n\t\t\t\tEl promedio General: {promedio_grupal:.2f}\n")
        else:
            print("\t\t\t\t⚠  No hay calificaciones registradas.\n")
        cursor.close()
        conexion.close()
