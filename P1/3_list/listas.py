#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
import os
os.system("cls")
numeros=[22,99,45]

print(numeros)

lista="["
for i in numeros:
    lista+=f"{i},"
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print(f"{lista}")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")

#1er forma 
palabras = ["hola", "2023", "hola que tal, soy colosal"]
palabra_buscar = input("Introduce la palabra a buscar: ")
if palabra_buscar in palabras:
    print("La palabra se encuentra en la lista")
else:
    print("La palabra no se encuentra en la lista")
#2da forma
for i in palabras:
    if i == palabra_buscar:
        print("La palabra se encuentra en la lista")
        break
    else:
        print("La palabra no se encuentra en la lista")
        break
#3ra forma
posicion = [i]
encontro = False
for i in range(0, len(palabras)):
    if palabras[i] == palabra_buscar:
        print("La palabra se encuentra en la lista")
        encontro = True
        posicion.append(i)
        break
if not encontro:
    palabras.append(palabra_buscar)
    print("La palabra no se encuentra en la lista, se ha añadido a la lista")


#Ejemplo 3 Añadir elementos a la lista
numeros = []
opc = "si"
while opc=="si":
    opc = input("¿Desea añadir un numero a la lista? (si/no): ").lower()
    numeros.append(float(input("Introduce un numero entero o decimal: ")))
print("Lista de numeros:", numeros)


#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda 
agenda = []
while True:
    nombre = input("Introduce el nombre: ")
    telefono = input("Introduce el telefono: ")
    agenda.append([nombre, telefono])
    continuar = input("¿Desea añadir otro contacto? (si/no): ").lower()
    if continuar != "si":
        break
print("Agenda de contactos:")
for contacto in agenda:
    print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}")

