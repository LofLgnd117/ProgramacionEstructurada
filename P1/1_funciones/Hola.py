#version 2 
numero=int(input("Dame el numero de la tabla de multiplicar a calcular: ")) 
for i in range(1,11): 
    multi=numero*i
print(f"{numero} x {i} = {multi}")

numero=int(input ("Dame el numero de la tabla de multiplicar a calcular: ")) 
i=1

while i<=10:
    multi=numero*i
print(f"{numero} x {i} = {multi}") 
i+=1
#version 3
def tabla(numero): 
    num=numero 
    respuesta="" 
    for i in range(1,11): 
        multi=num*i 
        espuesta+=f"\t{num} x {i} = {multi}\n"
numero=int(input("Dame numero de la tabla de multiplicar a c calcular: "))
print(f"Tabla de multiplicar del {numero}") 
resultado=tabla(numero) 
print(f"{resultado}")