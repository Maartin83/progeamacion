unidad = int(input("Ingresar cantidad a comprar: "))
#Condicion para obtener el precio
if unidad >=1 and unidad <=25:
 precio = 27
elif unidad >=26 and unidad <=50:
 precio = 25
else:
 precio = 23

#Calculando el importe de compra
importe = unidad * precio

#Condicion para el descuento
if unidad > 50:
 dscto = importe * 0.15
else:
 dscto = importe * 0.05

#Calculando el total a pagar
total = importe - dscto

print("Importe:",importe)
print("Descuento:",dscto)
print("Total:",total)
