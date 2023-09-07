monto=float(input("Ingrese monto:  "))
if monto>=500:
    descuento=monto*0.30
elif monto<500 and monto>=200:
    descuento = monto*0.20
elif monto>200 and monto>=100:
    descuento =monto*0.10
else:
    descuento = 0
    print("Sin descuento")
montof=monto-descuento
print("El descuento es:",descuento)
print("El monto final es:",montof)
