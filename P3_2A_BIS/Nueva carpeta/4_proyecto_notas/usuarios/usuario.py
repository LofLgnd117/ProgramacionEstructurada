from conexionBD import *
import datetime

def registrar(nombre,apellido,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, email, contraseña, fecha_registro) VALUES (%s, %s, %s, %s, %s)",{nombre, apellido, email, contrasena, fecha})
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contrasena):
    try:
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contraseña = %s", (email, contrasena))
        return cursor.fetchone()  # Retorna el primer usuario que coincida 
    except:
        return[]