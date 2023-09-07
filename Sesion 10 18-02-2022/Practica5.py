###Un supermercado ha puesto en oferta la venta al por mayor de cierto producto,
###ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.
###Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3.
###Diseñe un algoritmo que determine el monto de la compra,
##el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.
cantidad=int(input("Cantidad en docenas: "))
monto=float(input("Monto a pagar: "))
if cantidad>3:
    descuento=0.15
else:descuento=0.10
if cantidad>3:
    obsequio=cantidad-3
else:obsequio=0
descuentodemonto=(monto*descuento)
montofinal=monto-descuentodemonto
print("****************************")
print("Detalle de compra")
print("****************************")   
print("Monto de la compra:",monto)
print("Monto de descuento:",descuentodemonto)
print("Monto a pagar",montofinal)
print("Numero de obsequios:",obsequio)
