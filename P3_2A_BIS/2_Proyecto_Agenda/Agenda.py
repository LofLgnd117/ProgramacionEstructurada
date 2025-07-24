# Agenda.py (versión con MySQL integrada)
import os
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def borrarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperartecla():
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

def agregarcontacto():
    borrarpantalla()
    print("--- ➕ AGREGAR CONTACTO ➕ ---")
    nombre = input("Nombre: ").upper().strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM agenda WHERE nombre=%s", (nombre,))
        existe = cursor.fetchone()
        if existe:
            print("\n\t\t⚠️ ¡Este contacto ya existe! ⚠️")
        else:
            telefono = input("Teléfono: ").strip()
            email = input("Correo (email): ").lower().strip()
            cursor.execute("INSERT INTO agenda (nombre, telefono, email) VALUES (%s, %s, %s)", (nombre, telefono, email))
            conexion.commit()
            print("\n\t\t✅ ¡Contacto agregado con éxito! ✅")
        cursor.close()
        conexion.close()

def mostrarcontactos():
    borrarpantalla()
    print("--- 📚 MOSTRAR CONTACTOS 📚 ---")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM agenda")
        contactos = cursor.fetchall()
        if not contactos:
            print("\n\t\tℹ️ No hay contactos en la agenda. ℹ️")
        else:
            print(f"{'NOMBRE':<20} {'TELÉFONO':<20} {'CORREO':<30}")
            print("-" * 70)
            for contacto in contactos:
                print(f"{contacto[0]:<20} {contacto[1]:<20} {contacto[2]:<30}")
        cursor.close()
        conexion.close()

def buscarcontacto():
    borrarpantalla()
    print("--- 🔍 BUSCAR CONTACTO 🔍 ---")
    nombre_buscado = input("Ingresa el nombre del contacto a buscar: ").strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = "SELECT * FROM agenda WHERE nombre LIKE %s"
        cursor.execute(sql, (f"%{nombre_buscado}%",))
        resultados = cursor.fetchall()
        if resultados:
            print("\n--- ✅ CONTACTOS ENCONTRADOS ✅ ---")
            print(f"{'NOMBRE':<20} {'TELÉFONO':<20} {'CORREO':<30}")
            print("-" * 70)
            for contacto in resultados:
                print(f"{contacto[0]:<20} {contacto[1]:<20} {contacto[2]:<30}")
        else:
            print("\n\t\t❌ No se encontraron coincidencias. ❌")
        cursor.close()
        conexion.close()

def modificarcontacto():
    borrarpantalla()
    print("--- 🔄 MODIFICAR CONTACTO 🔄 ---")
    nombre = input("Nombre del contacto a modificar: ").upper().strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM agenda WHERE nombre=%s", (nombre,))
        contacto = cursor.fetchone()
        if contacto:
            telefono = input("Nuevo teléfono: ").strip()
            email = input("Nuevo correo: ").lower().strip()
            cursor.execute("UPDATE agenda SET telefono=%s, email=%s WHERE nombre=%s", (telefono, email, nombre))
            conexion.commit()
            print("\n\t\t✅ Contacto modificado correctamente.")
        else:
            print("\n\t\t❌ Contacto no encontrado.")
        cursor.close()
        conexion.close()

def eliminarcontacto():
    borrarpantalla()
    print("--- 🚮 ELIMINAR CONTACTO 🚮 ---")
    nombre = input("Nombre del contacto a eliminar: ").upper().strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM agenda WHERE nombre=%s", (nombre,))
        contacto = cursor.fetchone()
        if contacto:
            cursor.execute("DELETE FROM agenda WHERE nombre=%s", (nombre,))
            conexion.commit()
            print("\n\t\t✅ Contacto eliminado correctamente.")
        else:
            print("\n\t\t❌ Contacto no encontrado.")
        cursor.close()
        conexion.close()