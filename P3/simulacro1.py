lista=[8,1,0,-10,8,23,34,23]

def ordenar():
    lista.sort()

def recorrer():
    numeros=""
    for i in lista:
      numeros+=str(i) 
      numeros=numeros+"," 
    return numeros  

print(lista)            
ordenar()
print(lista) 
cadena_numeros=recorrer()
print(cadena_numeros)