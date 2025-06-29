def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

def menu_principal():
    print("\t\t\t\t 📝 .::: SISTEMA DE CALIFICACIONES :::. 📝\n")
    print("\t\t\t\t\t 1️⃣  ➤  Agregar")
    print("\t\t\t\t\t 2️⃣  ➤  Mostrar")
    print("\t\t\t\t\t 3️⃣  ➤  Calcular Promedio")
    print("\t\t\t\t\t 4️⃣  ➤  Buscar")
    print("\t\t\t\t\t 5️⃣  ➤  Salir\n")
    opcion = input("\t\t\t\t\t🔍 Selecciona una opción de 1-4: ")
    return opcion

def agregar_calificacion(lista):
    borrarPantalla()
    print("\t\t\t\t📂 .::AGREGAR CALIFICACIONES::. 📂\n")
    nombre = input("\t\t\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"\n\t\t\t📝 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("\n\t\t\t\t❌ Ingrese un número valido ❌\n")
            except ValueError:
                print("\n\t\t\t\t❌ Ingrese un valor numérico ❌\n")
    lista.append([nombre] + calificaciones)
    print("\n\t\t\t\t\t🎉 Acción realizada con éxito\n")

def mostrar_calificaciones(lista):
    ancho = 115
    borrarPantalla()
    print("\t\t\t\t📂 .::MOSTRAR CALIFICACIONES::. 📂\n")
    if len(lista) > 0:
        print(f"\t\t\t\t{'::Nombre::':<15}{'::Calif1::':<12}{'Calif2::':<12}{'::Calif3::':<12}")
        print(("-" * 60).center(ancho))
        for fila in lista:
            print(f"\t\t\t\t{fila[0]:<15}{fila[1]:<12}{fila[2]:<12}{fila[3]:<12}")
        print(("-" * 60).center(ancho))
        cuantos = len(lista)
        print(f"\n\t\t\t\t Son {cuantos} alumnos\n")
    else:
        print("\t\t\t\t⚠  No hay calificaciones registradas.\n")

def calcular_promedio(lista):
    borrarPantalla()
    ancho = 90
    print("\t\t\t\t📂 .::PROMEDIO DE ALUMNOS::. 📂\n")
    if len(lista) > 0:
        print(f"\t\t\t\t{'::Nombre::':<15}{'::Promedio::':<12}")
        print(("-" * 32).center(ancho))
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"\t\t\t\t{nombre:<15}{promedio:<12.2f}")
            promedio_grupal += promedio
        print(("-" * 32).center(ancho))
        promedio_grupal = promedio_grupal / len(lista)
        print(f"\n\t\t\t\tEl promedio General: {promedio_grupal:.2f}\n")
    else:
        print("\t\t\t\t⚠  No hay calificaciones registradas.\n")