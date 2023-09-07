km=float(input("Ingrese numero de km recorridos: "))
preciofijo=300
if km>100 and km<500:
    kme=km-100
    precio=(kme*15)+preciofijo
elif km>500:
    kme=km-500
    precio=(kme*10)+preciofijo
igv=precio*0.18
preciof=igv+precio
print("Precio base:",precio)
print("IGV:",igv)
print("Monto a pagar por alquiler del vehiculo:",preciof)
