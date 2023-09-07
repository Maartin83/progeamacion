### Realiza un programa que pida el valor de 3 artículos y muestre el total y la media Aritmética ###
v1= float(input("Ingrese Valor del 1er articulo:  "))
v2= float(input("Ingrese Valor del 2do articulo:  "))
v3= float(input("Ingrese Valor del 3er articulo:  "))
suma=v1+v2+v3
media=suma/3
print("El total es {} y el promedio es {}".format(suma,round(media,2)))
