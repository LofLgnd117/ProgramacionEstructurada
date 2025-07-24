# Nota.py
import funciones
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_notas"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def menu_notas():
    opcion = True
    while opcion:
        funciones.borrarpantalla()
        print("\n\t:: Gestión de Notas ::\n")
        print("1. Crear Nota")
        print("2. Ver Notas")
        print("3. Borrar Nota")
        print("4. Salir")
        eleccion = input("Elige una opción: ").strip()

        if eleccion == "1":
            crear_nota()
        elif eleccion == "2":
            ver_notas()
        elif eleccion == "3":
            borrar_nota()
        elif eleccion == "4":
            opcion = False
        else:
            print("\n\tOpción inválida")
            funciones.esperartecla()

def crear_nota():
    funciones.borrarpantalla()
    print("\n\t:: Crear Nota ::\n")
    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO notas (titulo, contenido) VALUES (%s, %s)", (titulo, contenido))
            conexion.commit()
            print("\n\tNota guardada correctamente.")
        except Error as e:
            print(f"\n\tError al guardar la nota: {e}")
        finally:
            cursor.close()
            conexion.close()
        funciones.esperartecla()

def ver_notas():
    funciones.borrarpantalla()
    print("\n\t:: Lista de Notas ::\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()
        if notas:
            for nota in notas:
                print(f"\nID: {nota[0]}\nTítulo: {nota[1]}\nContenido: {nota[2]}\n{'-'*30}")
        else:
            print("\n\tNo hay notas registradas.")
        cursor.close()
        conexion.close()
        funciones.esperartecla()

def borrar_nota():
    funciones.borrarpantalla()
    print("\n\t:: Borrar Nota ::\n")
    idnota = input("Ingresa el ID de la nota a borrar: ").strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM notas WHERE id=%s", (idnota,))
        nota = cursor.fetchone()
        if nota:
            cursor.execute("DELETE FROM notas WHERE id=%s", (idnota,))
            conexion.commit()
            print("\n\tNota eliminada correctamente.")
        else:
            print("\n\tNota no encontrada.")
        cursor.close()
        conexion.close()
        funciones.esperartecla()
