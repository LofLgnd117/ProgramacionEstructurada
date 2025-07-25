import Agenda
def main():
    import os
    agenda_contactos = {}
    opcion = True

    while opcion:
        os.system('cls')
        print("\n\t\t\t 📞.:::GESTIÓN DE CONTACTOS:::.\📞 \n\t1️⃣1.-Agregar contacto \n\t2️⃣2.-Mostrar todos los contactos \n\t3️⃣3.-Buscar contacto por nombre" \
        "\n\t4️⃣4.-Modifcar \n\t5️⃣5.-Eliminar \n\t6️⃣6.-SALIR")
        opcion = input("\n\t\t Elige una opción: ").upper()
        if opcion == "1":
            os.system('cls')
            Agenda.AgregarContacto(agenda_contactos)
            Agenda.esperar_tecla()
        elif opcion == "2":
            os.system('cls')
            Agenda.MostrarContactos(agenda_contactos)
            Agenda.esperar_tecla()
        elif opcion == "3":
            os.system('cls')
            Agenda.BuscarContacto(agenda_contactos)
            Agenda.esperar_tecla()
        elif opcion == "4":
            os.system('cls')
            Agenda.ModificarContacto(agenda_contactos)
            Agenda.esperar_tecla()
        elif opcion == "5":
            os.system('cls')
            Agenda.EliminarContacto(agenda_contactos)
            Agenda.esperar_tecla()    
        elif opcion == "6":
            print("\n\t\t\t 🚪.:::HASTA LUEGO:::.\🚪")
            Agenda.esperar_tecla()
            opcion = False
        else:
            print("\n\t\t\t ❌.:::OPCIÓN INVÁLIDA:::.\❌")
            input("\n\t\t ✨Presiona Enter para continuar...✨")

if __name__ == "__main__":
    main()