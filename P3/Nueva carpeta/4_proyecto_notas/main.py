import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
              menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
              print(f"\n\tE-mail y/o contraseña incorrectas por favor verifique ....")
              funciones.esperarTecla()    
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta = nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"\n\tNota creada correctamente.")
            else:
                print(f"\n\tNo se pudo crear la nota, intente más tarde.")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            print(f"\n \t .:: Mostrar Notas ::. ")
            notas = nota.mostrar(usuario_id)
            if notas:
                print("\n\t\t Notas del Usuario:")
                for nota_item in notas:
                    print(f"\tID: {nota_item[0]}, Título: {nota_item[2]}, Descripción: {nota_item[3]}")
            else:
                print("\n\tNo hay notas para mostrar.")
            print("\n\tPresiona cualquier tecla para continuar...")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            respuesta = nota.cambiar(id, titulo, descripcion)
            if respuesta:
                mostras = nota.mostrar(usuario_id)
                print("\n\tNotas actualizadas:")
                print(f"{'ID':<10}{'Título':<15}{'Descripción':<30}")
                print(f"-" * 80)
                for fila in mostras:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}")
                print(f"-" * 80)
                funciones.esperarTecla()
                print(f"\n\tNota actualizada correctamente.")
            else:
                print(f"\n\tNo se pudo actualizar la nota, intente más tarde.")
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print("\n\tNotas actualizadas:")
            print(f"{'ID':<10}{'Título':<15}{'Descripción':<30}")
            print(f"-" * 80)
            for fila in mostras:
                print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}")
                print(f"-" * 80)
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t desea eliminar una nota? Si/No: ").strip().upper()
            if id == "SI":
                id = input("\t \t ID de la nota a eliminar: ")
            else:
                print("\n\tNo se eliminará ninguna nota.")
                funciones.esperarTecla()
                continue
            funciones.esperarTecla()
            #Agregar codigo
            respuesta = nota.eliminar(id)
            if respuesta:
                print("\n\tNotas actualizadas:")
                print(f"{'ID':<10}{'Título':<15}{'Descripción':<30}")
                print(f"-" * 80)
                for fila in mostras:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<30}")
                    print(f"-" * 80)
                print(f"\n\tNota {id} eliminada correctamente.")
            else:
                print(f"\n\tNo se pudo eliminar la nota, intente más tarde.")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


