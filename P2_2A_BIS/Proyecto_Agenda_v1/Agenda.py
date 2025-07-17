import os

def BorrarPantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls')

def EsperarTecla():
    """Pausa la ejecución del programa hasta que se presione una tecla."""
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

def AgregarContacto(Agenda):
    """
    Agrega un nuevo contacto a la agenda.
    Si el contacto ya existe, muestra un mensaje.
    """
    BorrarPantalla()
    print("--- ➕ AGREGAR CONTACTO ➕ ---")
    nombre = input("Nombre: ").upper().strip() # Added space for better UX
    if nombre in Agenda:
        print("\n\t\t⚠️ ¡Este contacto ya existe! ⚠️")
    else:
        telefono = input("Teléfono: ").strip() # Changed variable name for consistency, removed .upper() as phone numbers are not typically uppercase
        correo = input("Correo (email): ").lower().strip() # Changed to .lower() for emails
        Agenda[nombre] = [telefono, correo] # <<< CRITICAL FIX: Storing the contact
        print("\n\t\t✅ ¡Contacto agregado con éxito! ✅")

def MostrarContactos(Agenda):

    BorrarPantalla()
    print("--- 📚 MOSTRAR CONTACTOS 📚 ---")
    if not Agenda:
        print("\n\t\tℹ️ No hay contactos en la agenda. ℹ️")
    else:
        # Corrected header printing
        print(f"{"NOMBRE":<20} {"TELÉFONO":<20} {"CORREO":<30}")
        print("-" * 70) # Adjusted length for new column widths
        for nombre, info in Agenda.items(): # Changed lista to info for clarity
            print(f"{nombre:<20} {info[0]:<20} {info[1]:<30}")

def BuscarContacto(Agenda):
    BorrarPantalla()
    print("--- 🔍 BUSCAR CONTACTO 🔍 ---")
    nombre_buscado = input("Ingresa el nombre del contacto a buscar: ").strip()
    
    encontrados = {
        n: info for n, info in Agenda.items()
        if nombre_buscado.lower() in n.lower()
    }
    
    if encontrados:
        print("\n--- ✅ CONTACTOS ENCONTRADOS ✅ ---")
        # Reuse the display logic from MostrarContactos for consistency
        print(f"{"NOMBRE":<20} {"TELÉFONO":<20} {"CORREO":<30}")
        print("-" * 70)
        for nombre, info in encontrados.items():
            print(f"{nombre:<20} {info[0]:<20} {info[1]:<30}")
    else:
        print("\n\t\t❌ No se encontraron coincidencias. ❌")

