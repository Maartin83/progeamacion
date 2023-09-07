###Desarrolle el programa que determine si un numero de 3 cifras en capicúa o no
numero=int(input("Ingrese numero:  "))
d1=numero//100
r1=numero%100
d2=r1//10
d3=r1%10
inv=d3*100+d2*10+d3*1
if numero==inv:
    print("El numero",numero, "es capicua")
else: print("El numero",numero, "no es capicua")
