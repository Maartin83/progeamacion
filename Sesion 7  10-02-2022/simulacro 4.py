###Hacer un programa que ingresado el costo de los medicamentos
###calcule el descuento y el precio final. (Descuento es el 10% del costo)
v1=float(input("Ingrese costo de los medicamentos:  "))
descuento=0.10
desfin=v1*descuento
total=v1-desfin
print("El descuento es de {} y el precio final seria {}".format(round(desfin,2),total))

