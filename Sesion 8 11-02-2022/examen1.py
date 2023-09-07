###Escribir un programa que calcule el salario de un trabajador de la manera siguiente.
###El trabajador cobra un precio fijo por hora y se le descuento el 15% en concepto de impuesto sobre la renta.
###El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio que cobra por hora.
###Como salida debe imprimir el sueldo bruto, el descuento de renta y el salario a pagar
nombre=input("Ingrese nombre del trabajador:  ")
horas=float(input("Ingrese horas trabajadas:  "))
precioxh=float(input("Precio de cobro por hora:  "))
sueldobruto=horas*precioxh
descuento=sueldobruto*0.15
salariof=sueldobruto-descuento
print("Sueldo bruto:{} desceunto de renta:{} salario a pagar:{} ".format(sueldobruto,descuento,salariof))
