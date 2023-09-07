precio_k=float(input("Ingrese precio por kl.: "))
peso=float(input("Ingrese el peso en kl.: "))
preciobase=precio_k*peso
if peso>0 and peso<=2:
    descuento=0
elif peso>2 and peso<=5:
    descuento=0.10*preciobase
elif peso>5 and peso<=10:
    descuento=0.15*preciobase
else: descuento=0.20*preciobase
total=preciobase+descuento
print("Precio base:",preciobase)
print("Descuento:",descuento)
print("Total a pagar:",total)
