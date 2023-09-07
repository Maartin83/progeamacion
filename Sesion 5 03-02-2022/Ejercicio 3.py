"""Escriba un programa que permita obtener el monto en dólares de un monto en soles
ingresado por el usuario"""
###CONSTANTES:Es un identificador cuyo valor no cambia en el proceso de un algoritmo
TIPO_CAMBIO = 3.86
soles = float(input("Ingrese monto en soles:  "))
dolares = soles / TIPO_CAMBIO
print("El monto en dolares es:  ",dolares)
