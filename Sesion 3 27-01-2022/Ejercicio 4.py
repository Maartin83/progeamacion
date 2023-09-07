"""Realiza un programa que pida el valor de 3 artículos y muestre el total y la media Aritmética"""

articulo1 = float(input("Valor de Articulo 1:  "))
articulo2 = float(input("Valor de Articulo 2:  "))
articulo3 = float(input("Valor de Articulo 3:  "))

ValorF = articulo1 + articulo2 + articulo3
media = ValorF / 3

print("Valor Total:  ",ValorF)
print("Promedio:  ",media)
