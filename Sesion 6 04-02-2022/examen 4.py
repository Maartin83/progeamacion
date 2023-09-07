#4.Diseñar un algoritmo que lea cuatro variables
#y calcule e imprima su producto, suma y media aritmética.
v1=float(input("Ingrese primera variable:  "))
v2=float(input("Ingrese segunda variable:  "))
v3=float(input("Ingrese tercera variable:  "))
v4=float(input("Ingrese cuarta variable:  "))
producto=v1*v2*v3*v4
suma=v1+v2+v3+v4
promedio=suma/4
print("Producto:{} Suma:{} Media aritmetrica:{}".format(producto,suma,promedio))
