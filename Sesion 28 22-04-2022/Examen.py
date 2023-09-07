horas=float(input("Ingrese horas trabajadas: "))
area=input("Ingrese Area: ")
aream=area.lower()
def sueldobruto(horas,area):
	if aream=="sistemas":
		sueldob=horas*21
	if aream=="rr.hh":
		sueldob=horas*19.5
	if aream=="administrativo":
		sueldob=horas*17
	if aream=="limpieza":
		sueldob=horas*10
	return(sueldob)
def descuento(sueldob):
	if sueldob>2500:
		descuento=sueldob*0.20
	else:
		descuento=sueldob*0.15
	return(descuento)
print("*********************************")
print("El sueldo bruto es:",sueldobruto(horas,aream))
print("El descuento es:",descuento(sueldobruto(horas,aream)))
print("El sueldo neto seria:",sueldobruto(horas,aream)-descuento(sueldobruto(horas,aream)))