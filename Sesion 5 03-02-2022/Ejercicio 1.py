"""Escriba un programa en python que permita calcular el aréa de un cuadrado
con los valores ingresados por el usuario. La formula para obtener el area de un
cuadrado es lado2"""

lado = float(input("Ingresar el lado del cuadrado:  "))
area = lado**2
perimetro = lado*4
print("El area del cuadrado es {},y el perimetro es {}".format(area,perimetro))

