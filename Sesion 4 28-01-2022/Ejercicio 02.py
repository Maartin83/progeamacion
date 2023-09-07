#Ingresarun numero de 3 digitos; crear un algoritmo para sumar sus digitos
numero = int(input("ingresar nunmero:  "))
d1 = numero//100
r1 = numero%100
d2 = r1//10
d3 = r1%10

suma = d1 + d2 + d3
print("Suma de digitos:  ",suma)
