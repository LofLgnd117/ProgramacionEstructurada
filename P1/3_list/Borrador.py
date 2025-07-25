palabras = ["hola", "adios", "gracias", "por favor", "buenos dias"]
palabra_buscar = input("Introduce la palabra a buscar: ")

encontro= False
cuantas = 0
posicion = 0
for i in palabras:
    if i == palabra_buscar:
        print("La palabra se encuentra en la lista")
        encontro = True
        cuantas+=1
        posicion.append(palabras.index(i))
        if encontro:
            print("La palabra se encuentra en la lista")
            break
    else:
        print("La palabra no se encuentra en la lista")
        break