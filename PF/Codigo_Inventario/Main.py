import tienda
import sys

def main():
    usuario_id = tienda.login()
    if not usuario_id:
        print("🔒 Inicio de sesión fallido. Saliendo.")
        return

    try:
        while True:
            tienda.borrar_pantalla()
            print(f"\n✅ ¡Bienvenido, usuario {usuario_id}!") 
            print("\n💼 .:: MENÚ PRINCIPAL DE INVENTARIO ::. 💼\n")
            print("1️⃣  Inventario")
            print("2️⃣  Salir")

            opcion_menu = input("\n🔎 Selecciona una opción: ").strip()

            if opcion_menu == "1":
                submenu_inventario(usuario_id)
            elif opcion_menu == "2":
                print("\n👋 Gracias por utilizar el sistema. Hasta pronto!")
                break
            else:
                print("\n❌ Opción inválida.")
                tienda.esperar_tecla()

    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. Saliendo...")
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

def submenu_inventario(usuario_id):
    while True:
        tienda.borrar_pantalla()
        print("\n📦 .:: GESTIÓN DE INVENTARIO ::. 📦\n")
        print("1️⃣  Agregar componente")
        print("2️⃣  Mostrar inventario")
        print("3️⃣  Buscar componente")
        print("4️⃣  Modificar componente (otros datos)")
        print("5️⃣  Eliminar componente")
        print("6️⃣  Exportar a PDF")
        print("7️⃣  Modificar estado del componente")
        print("8️⃣  Volver al menú principal")

        eleccion = input("\n🔎 Selecciona una opción: ").strip()

        if eleccion == "8":
            break
        
        if eleccion == "1":
            tienda.agregar_componente(usuario_id)
        elif eleccion == "2":
            tienda.mostrar_inventario()
        elif eleccion == "3":
            tienda.buscar_componente()
        elif eleccion == "4":
            tienda.modificar_componente()
        elif eleccion == "5":
            tienda.eliminar_componente()
        elif eleccion == "6":
            tienda.exportar_a_pdf()
        elif eleccion == "7":
            tienda.modificar_estado_componente()
        else:
            print("\n❌ Opción inválida.")

        tienda.esperar_tecla()

if __name__ == "__main__":
    main()