###Leer un numero de 4 cifras, mostrar como resultado la cifra mayor y meno
v1=int(input("Ingrese el numero de 4 cifras  "))
d1=v1//1000
r1=v1%1000

d2=r1//100
r2=r1%100

d3=r2//10
d4=r2%10

minimo=min(d1,d2,d3,d4)
maximo=max(d1,d2,d3,d4)
print("La cifra mayor del numero es:{} y el menor es:{}".format(maximo,minimo))

