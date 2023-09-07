#5. Un vendedor recibe mensualmente un sueldo base más un 10% extra por comisión de sus ventas.
#El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
#y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones
sueldo=float(input("Ingrese sueldo:  "))
comision=0.10*sueldo
comisionalmes=comision*3
total=sueldo+comisionalmes
print("Comision por las 3 ventas:  ",comisionalmes)
print("Sueldo total:  ",total)
