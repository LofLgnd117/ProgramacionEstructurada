# USUARIO.py
import mysql.connector
from mysql.connector import Error
import funciones

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

def registrar_usuario():
    funciones.borrarpantalla()
    print("\n\t:: Registro de Usuario ::\n")
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    password = input("Contraseña: ").strip()

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, correo, password) VALUES (%s, %s, %s)", (nombre, correo, password))
            conexion.commit()
            print("\n\tUsuario registrado exitosamente.")
        except Error as e:
            print(f"\n\tError al registrar usuario: {e}")
        finally:
            cursor.close()
            conexion.close()
        funciones.esperartecla()

def login():
    funciones.borrarpantalla()
    print("\n\t:: Login de Usuario ::\n")
    correo = input("Correo: ").strip()
    password = input("Contraseña: ").strip()

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s AND password=%s", (correo, password))
        usuario = cursor.fetchone()
        if usuario:
            print(f"\n\tBienvenido {usuario[1]}!")
            cursor.close()
            conexion.close()
            funciones.esperartecla()
            return True
        else:
            print("\n\tCredenciales incorrectas.")
            cursor.close()
            conexion.close()
            funciones.esperartecla()
            return False
    else:
        funciones.esperartecla()
        return False