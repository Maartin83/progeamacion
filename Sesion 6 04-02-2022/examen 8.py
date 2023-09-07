#8. Una institución social recibe anualmente una donación que reparte de la
#siguiente forma: 25% para el centro de salud, 35% en el comedor infantil, 25% para la escuela infantil
#y el resto para el asilo de ancianos.Desarrolle el programa que muestre los montos asignados.
donacion=float(input("Ingresar monto de la donacion:  "))
cds=donacion*0.25
ci=donacion*0.35
ei=donacion*0.25
ada=donacion*0.15
print("El mondo para centro de salud es:  ",cds)
print("El mondo para comedor infantil es:  ",ci)
print("El mondo escuela infantil es:  ",ei)
print("El mondo asilo de ancianos es:  ",ada)
