#Ingresar 2 valores numericos, y mostrar como resultado las 4 operaciones
#Matematicas
numero1 = int(input("Ingresar numero 1: "))
numero2 = int(input("Ingresar numero 2: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division =numero1 / numero2

print("la suma es:  ",suma)
print("la resta es:  ",resta)
print("la multiplicacion es:  ",multiplicacion)
print("la division es:  ",round(division,2))
