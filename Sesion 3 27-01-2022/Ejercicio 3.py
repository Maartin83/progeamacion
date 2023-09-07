"""Progrma que pida el precio de un articulo y calcule su valor aplicandole un 10%
de IGV. """

precio = float(input("Ingresar precio del articulo:  "))
IGV = precio * 0.18
precioF = precio + IGV

print("IGV:  ",IGV)
print("Precio Final:  ",precioF)
