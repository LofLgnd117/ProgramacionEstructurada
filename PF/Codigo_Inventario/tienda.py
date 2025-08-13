import os
import mysql.connector
from mysql.connector import Error
import getpass
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import datetime

def conectar():
    """Establece la conexión con la base de datos."""
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_inventario"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

def borrar_pantalla():
    """Borra la pantalla de la consola."""
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    """Pausa la ejecución hasta que el usuario presione una tecla."""
    input("\n⏳ Presiona cualquier tecla para continuar... ⌛")

def registrar_usuario():
    """Permite el registro de un nuevo usuario."""
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n📝 Registro de nuevo usuario")
    while True:
        username = input("👤 Nombre de usuario: ").strip()
        if username:
            break
        print("❌ El nombre de usuario no puede estar vacío.")

    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        correo = input("📧 Correo electrónico: ").strip()
        if not re.match(patron_email, correo):
            print("❌ Formato de correo inválido.")
            continue
        cursor.execute("SELECT id_usuario FROM usuarios WHERE correo = %s", (correo,))
        if cursor.fetchone():
            print("❌ Ese correo ya está registrado.")
        else:
            break

    while True:
        password = getpass.getpass("🔑 Contraseña: ").strip()
        if password:
            break
        print("❌ La contraseña no puede estar vacía.")

    cursor.execute(
        "INSERT INTO usuarios (username, correo, password) VALUES (%s, %s, %s)",
        (username, correo, password)
    )
    conexion.commit()
    print("✅ Usuario registrado con éxito.")
    cursor.close()
    conexion.close()

def login():
    """Maneja el inicio de sesión del usuario."""
    while True:
        borrar_pantalla()
        print("\n🔐 .:: INICIO DE SESIÓN ::. 🔐\n")
        print("1️⃣  Iniciar sesión")
        print("2️⃣  Crear nuevo usuario")
        print("3️⃣  Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            usuario = input("👤 Usuario: ").strip()
            password = getpass.getpass("🔑 Contraseña: ").strip()

            conexion = conectar()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT id_usuario FROM usuarios WHERE username=%s AND password=%s", (usuario, password))
                user = cursor.fetchall()
                cursor.close()
                conexion.close()
                if user:
                    print("\n✅ Inicio de sesión exitoso ✅")
                    esperar_tecla()
                    return user[0][0]
                else:
                    print("\n❌ Usuario o contraseña incorrectos ❌")
                    esperar_tecla()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            return False
        else:
            print("\n❌ Opción inválida")
            esperar_tecla()

def mostrar_estados():
    """Muestra todos los estados disponibles."""
    print("\n📜 .:: ESTADOS DISPONIBLES ::. 📜\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_estados, Estados FROM estados")
        estados = cursor.fetchall()
        if estados:
            print(f"{'🆔 ID':<5}{'📝 Nombre':<20}")
            print("-" * 25)
            for fila in estados:
                print(f"{fila[0]:<5}{fila[1]:<20}")
        else:
            print("\nℹ️ No hay estados registrados.")
        cursor.close()
        conexion.close()

def agregar_componente(id_usuario):
    """Agrega un nuevo componente al inventario."""
    borrar_pantalla()
    print("\n➕ .:: AGREGAR COMPONENTE ::. ➕\n")
    while True:
        nombre = input("💻 Nombre del componente: ").strip().upper()
        if nombre: break
        print("❌ Este campo no puede estar vacío.")

    while True:
        marca = input("⭐ Marca del componente: ").strip().upper()
        if marca: break
        print("❌ Este campo no puede estar vacío.")

    while True:
        descripcion = input("📄 Descripción: ").strip().upper()
        if descripcion: break
        print("❌ Este campo no puede estar vacío.")

    while True:
        try:
            cantidad = int(input("🔢 Cantidad en inventario: ").strip())
            break
        except ValueError:
            print("❌ Cantidad no válida.")
            
    while True:
        try:
            precio = float(input("💲 Precio: ").strip())
            break
        except ValueError:
            print("❌ Precio no válido.")

    mostrar_estados()
    while True:
        try:
            id_estado = int(input("🆔 Ingresa el ID del estado: ").strip())
            break
        except ValueError:
            print("❌ ID de estado no válido.")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO inventario (nombre, cantidad, descripcion, precio, id_usuario, id_estados, marca)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nombre, cantidad, descripcion, precio, id_usuario, id_estado, marca))
            conexion.commit()
            print("\n✅ Componente agregado correctamente.")
        except Error as e:
            print(f"\n❌ Error: {e}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_inventario():
    """Muestra todos los componentes en el inventario."""
    borrar_pantalla()
    print("\n📦 .:: INVENTARIO ::. 📦\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_componente, nombre, marca, descripcion, cantidad, precio, Estados FROM inventario INNER JOIN estados ON inventario.id_estados = estados.id_estados")
        datos = cursor.fetchall()
        if datos:
            print(f"{'🆔 ID':<5} {'💻 Nombre':<25} {'⭐ Marca':<15} {'📄 Descripción':<25} {'🔢 Cantidad':<10} {'💲 Precio':<10} {'📝 Estado':<10}")
            print("="*125)
            for fila in datos:
                print(f"{fila[0]:<5} {fila[1]:<25} {fila[2]:<15} {fila[3]:<25} {fila[4]:<10} {fila[5]:<10} {fila[6]:<10}")
        else:
            print("\nℹ️ No hay componentes registrados.")
        cursor.close()
        conexion.close()

def buscar_componente():
    """Busca un componente en el inventario por su nombre."""
    borrar_pantalla()
    print("\n🔍 .:: BUSCAR COMPONENTE ::. 🔍\n")
    while True:
        nombre = input("🔎 Nombre a buscar: ").strip().upper()
        if nombre: break
        print("❌ El campo de búsqueda no puede estar vacío.")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_componente, nombre, marca, descripcion, cantidad, precio, Estados FROM inventario INNER JOIN estados ON inventario.id_estados = estados.id_estados WHERE nombre LIKE %s", (f"%{nombre}%",))
        datos = cursor.fetchall()
        if datos:
            print(f"{'🆔 ID':<5} {'💻 Nombre':<25} {'⭐ Marca':<15} {'📄 Descripción':<25} {'🔢 Cantidad':<10} {'💲 Precio':<10} {'📝 Estado':<10}")
            print("="*125)
            for fila in datos:
                print(f"{fila[0]:<5} {fila[1]:<25} {fila[2]:<15} {fila[3]:<25} {fila[4]:<10} {fila[5]:<10} {fila[6]:<10}")
        else:
            print("\n❌ No se encontraron coincidencias.")
        cursor.close()
        conexion.close()

def modificar_componente():
    """Modifica los datos de un componente existente."""
    borrar_pantalla()
    print("\n✏️ .:: MODIFICAR COMPONENTE ::. ✏️\n")
    mostrar_inventario()
    while True:
        id_comp = input("\n🆔 Ingresa el ID del componente a modificar: ").strip()
        if id_comp.isdigit(): break
        print("❌ Ingresa un ID válido (número).")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id_componente = %s", (id_comp,))
        comp = cursor.fetchone()
        if comp:
            print(f"Actual: ID={comp[0]} | Nombre={comp[1]} | Marca={comp[7]} | Descripción={comp[3]} | Cantidad={comp[2]} | Precio={comp[4]}")
            print("\n🔧 ¿Qué deseas modificar?")
            print("1️⃣ Nombre\n2️⃣ Marca\n3️⃣ Descripción\n4️⃣ Cantidad\n5️⃣ Precio")
            opcion = input("Selecciona una opción: ").strip()
            
            if opcion == "1":
                nuevo = input("💻 Nuevo nombre: ").strip().upper()
                if not nuevo:
                    print("❌ Campo vacío. No se realizaron cambios.")
                    return
                cursor.execute("UPDATE inventario SET nombre=%s WHERE id_componente=%s", (nuevo, id_comp))
            elif opcion == "2":
                nuevo = input("⭐ Nueva marca: ").strip().upper()
                if not nuevo:
                    print("❌ Campo vacío. No se realizaron cambios.")
                    return
                cursor.execute("UPDATE inventario SET marca=%s WHERE id_componente=%s", (nuevo, id_comp))
            elif opcion == "3":
                nuevo = input("📄 Nueva descripción: ").strip().upper()
                if not nuevo:
                    print("❌ Campo vacío. No se realizaron cambios.")
                    return
                cursor.execute("UPDATE inventario SET descripcion=%s WHERE id_componente=%s", (nuevo, id_comp))
            elif opcion == "4":
                while True:
                    try:
                        nuevo = int(input("🔢 Nueva cantidad: ").strip())
                        break
                    except ValueError:
                        print("❌ Ingresa un número válido")
                cursor.execute("UPDATE inventario SET cantidad=%s WHERE id_componente=%s", (nuevo, id_comp))
            elif opcion == "5":
                while True:
                    try:
                        nuevo = float(input("💲 Nuevo precio: ").strip())
                        break
                    except ValueError:
                        print("❌ Ingresa un número válido")
                cursor.execute("UPDATE inventario SET precio=%s WHERE id_componente=%s", (nuevo, id_comp))
            else:
                print("❌ Opción no válida")
                return

            conexion.commit()
            print("\n✅ Componente modificado exitosamente.")
        else:
            print("\n❌ ID no encontrado.")
        cursor.close()
        conexion.close()

def modificar_estado_componente():
    """Modifica el estado de un componente existente."""
    borrar_pantalla()
    print("\n🔄 .:: MODIFICAR ESTADO DE COMPONENTE ::. 🔄\n")
    mostrar_inventario()
    while True:
        id_comp = input("\n🆔 Ingresa el ID del componente a modificar: ").strip()
        if id_comp.isdigit(): break
        print("❌ Ingresa un ID válido (número).")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id_componente = %s", (id_comp,))
        comp = cursor.fetchone()
        if comp:
            mostrar_estados()
            while True:
                try:
                    nuevo_estado = int(input("🆔 Ingresa el nuevo ID de estado: ").strip())
                    break
                except ValueError:
                    print("❌ Ingresa un ID de estado válido.")
            cursor.execute("UPDATE inventario SET id_estados=%s WHERE id_componente=%s", (nuevo_estado, id_comp))
            conexion.commit()
            print("\n✅ Estado del componente modificado exitosamente.")
        else:
            print("\n❌ ID no encontrado.")
        cursor.close()
        conexion.close()

def eliminar_componente():
    """Elimina un componente del inventario."""
    borrar_pantalla()
    print("\n🗑️ .:: ELIMINAR COMPONENTE ::. 🗑️\n")
    mostrar_inventario()
    while True:
        id_comp = input("\n🆔 Ingresa el ID del componente a eliminar: ").strip()
        if id_comp.isdigit():
            break
        print("❌ Ingresa un ID válido (número).")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id_componente = %s", (id_comp,))
        comp = cursor.fetchone()
        if comp:
            confirmacion = input(f"⚠️ ¿Estás seguro que deseas eliminar el componente '{comp[1]}'? (s/n): ").strip().lower()
            if confirmacion == "s":
                cursor.execute("DELETE FROM inventario WHERE id_componente = %s", (id_comp,))
                conexion.commit()
                print("\n✅ Componente eliminado exitosamente.")
            else:
                print("\nℹ️ Operación cancelada.")
        else:
            print("\n❌ ID no encontrado.")
        cursor.close()
        conexion.close()
        
def exportar_a_pdf():
    """Exporta el inventario a un archivo PDF."""
    borrar_pantalla()
    print("\n📄 .:: EXPORTAR INVENTARIO A PDF ::. 📄\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_componente, nombre, marca, descripcion, cantidad, precio, Estados FROM inventario INNER JOIN estados ON inventario.id_estados = estados.id_estados")
        datos = cursor.fetchall()
        if not datos:
            print("ℹ️ No hay componentes para exportar.")
            return

        # Configuración del PDF
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_pdf = f"inventario_{fecha_actual}.pdf"
        doc = SimpleDocTemplate(nombre_pdf, pagesize=letter)
        estilos = getSampleStyleSheet()
        elementos = []

        # Título
        titulo = Paragraph("Inventario de Hardware", estilos['Title'])
        elementos.append(titulo)
        elementos.append(Spacer(1, 12))

        # Tabla de datos
        data = [["🆔 ID", "💻 Nombre", "⭐ Marca", "📄 Descripción", "🔢 Cantidad", "💲 Precio", "📝 Estado"]]
        for fila in datos:
            data.append([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]])

        tabla = Table(data)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        elementos.append(tabla)

        # Guardar el PDF
        doc.build(elementos)
        print(f"\n✅ Inventario exportado exitosamente a {nombre_pdf}.")
        
        cursor.close()
        conexion.close()
    else:
        print("❌ No se pudo conectar a la base de datos.")