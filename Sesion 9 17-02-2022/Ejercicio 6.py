nombre=input("Nombre del producto:  ")
precio=float(input("Precio del Producto:  "))
cantidad=int(input("Cantidad de Unidades:  "))
importe=precio*cantidad
if importe>1500:
    descuento=importe*0.10
else:
    descuento=importe*0.02
pagof=importe-descuento

print("Datos de Venta")
print("**************")
print("Producto",nombre)
print("Precio",precio)
print("Cantidad",cantidad)
print("Importe",importe)
print("Descuento",descuento)
print("Pago Final",pagof)
