###Un vendedor recibe mensualmente un sueldo base más un 10% extra por comisión de sus ventas.
###El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
###y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones
v1=float(input("sueldo base:  "))
comision=v1*0.10
comisiontotal=comision*3
total=comisiontotal+v1
print("Dinero por comisiones {} y el total es {}".format(round(comisiontotal,2),total))

    
