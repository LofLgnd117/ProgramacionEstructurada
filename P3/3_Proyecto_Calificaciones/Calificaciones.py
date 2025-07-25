# Calificaciones.py (integrado con MySQL)
import os
import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos MySQL, si no se me olvida si se la mandé a Vicoria xd
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

#Esto es solo para limpiar la pantalla despus de cada acción
def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#Igual es solo una funcion simple para esperar al usuario
def esperarTecla():
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

#Aqui se mandan a llamar las funciones de más abajo, es como un "submenú".
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
    #Lo que hay sirve para en primera crear la lista de calificaciones e ingresar el nombre y las calificaciones
    #aqui el profesor nos hizo hacerlo con un for
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
    #De aqui en adelante es para guardar las calificaciones en la base de datos
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO calificaciones (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)", #aqui yo puse "INSERT INTO" en mayusculas
                           (nombre, calificaciones[0], calificaciones[1], calificaciones[2]))               #pero el profesor lo puso en minusculas.
            conexion.commit()
            print("\n\t\t\t\t🎉 Acción realizada con éxito 🎉\n")
        except Error as e:
            print(f"\n\t\t\t\t❌ Error al guardar: {e}")
        finally:
            cursor.close() #aqui tengo la duda, no se si hay otra manera de evitar que se "destruya" el cursor, pero el profesor lo hizo asi vaya
            conexion.close()

def mostrar_calificaciones():
    ancho = 115
    borrarPantalla()
    print("\t\t\t\t📂 .::MOSTRAR CALIFICACIONES::. 📂\n")
    conexion = conectar()
    #Aqui se conecta a la base de datos y se pueden observar las calificaciones de los alumnos, no hay mucha ciencia en esta función
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
    #aqui se manda a llamar la base de datos y se calcula el promedio de cada alumno, la manera que nos enseñó el profesor
    #es la que se usa, no hubo modificaciones, aclaro que es el calculo para todos los alumnos, no solo para uno
    print("\t\t\t\t📂 .::PROMEDIO DE ALUMNOS::. 📂\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones") #Igual, aqui el profesor lo puso en minusculas
        registros = cursor.fetchall()#aqui se manda a llamar a todos los registros de la base de datos
        if registros:
            print(f"\t\t\t\t{'::Nombre::':<15}{'::Promedio::':<12}")
            print(("-" * 32).center(ancho))
            promedio_grupal = 0
            for fila in registros: #aqui se calcula el promedio de cada alumno
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
#En si esto es el codigo del módulo de Calificaciones, como haz de suponer no tenemos mucho conocimiento de MySQL y al menos de mi parte no mucho de
#listas y diccionarios, aunque lo que si debo aclarar es que el profesor no se da el tiempo a explicar bien los conceptos de listas y diccionarios.