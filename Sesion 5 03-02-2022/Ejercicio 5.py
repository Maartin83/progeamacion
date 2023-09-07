#Ingresar un numero y mostrar su raiz cuadrada y la potencia

import math

numero = int(input("Ingresar numero:  "))
raiz = math.sqrt(numero)
potencia = math.pow(numero,2)
print("La raiz cuadrada es: ",round(raiz,2))
print("la potencia al cuadrado es:  ",potencia)
