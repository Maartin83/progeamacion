#Ingresarun numero de 4 digitos; crear un algoritmo para sumar sus digitos
numero = int(input("ingresar nunmero:  "))
d1 = numero//1000
r1 = numero%1000
d2 = r1//100
r2 = r1%100
d3 = r2//10
d4 = r2%10
suma = d1 + d2 + d3 +d4
print("Suma de digitos:  ",suma)

