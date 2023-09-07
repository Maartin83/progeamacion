#Igresar un numero de dos digitos; crear un algoritmo para sumar sus digitos.
numero = int(input("ingresar numero:  "))

d1 = numero//10
d2 = numero%10

suma = d1 + d2

print("Suma de digitos  ",suma)
