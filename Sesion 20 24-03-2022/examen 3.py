nombre=input("Ingrese nombre del trabajador: ")
precio_horas=float(input("ingrese precio por hora de trabajo: "))
horas_trabajadas=float(input("Ingrese horas trabajadas: "))

if horas_trabajadas>40 and horas_trabajadas<=48:
	horas_extras=horas_trabajadas-40
	P_final=horas_extras*(precio_horas*2)
	
	print("Hola",nombre,"la cantidad de dinero que recibiras por concepto de horas extras es :",P_final)

if horas_trabajadas > 48:
	horas_extras_precio=(precio_horas*2)*8
	horas_extras_dobles=horas_trabajadas-48
	P_final=horas_extras_precio+(horas_extras_dobles*(precio_horas*3))
	
	print("Hola",nombre,"la cantidad de dinero que recibiras por concepto de horas extras es :",P_final )

