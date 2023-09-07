#Ingresarun numero de 4 digitos; crear un algoritmo para sumar sus digitos
numero = int(input("ingresar nunmero:    "))
d1 = numero//10000
r1 = numero%10000

d2 = r1//1000
r2 = d2%1000

d3 = r2//100
r3 = d3%100

d4 = r3//10
d5 = d4%10

suma = d1 + d2 + d3 + d4 + d5
print("Suma de digitos:  ",suma)
