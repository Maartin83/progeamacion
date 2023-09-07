while True:
	nombre=input("Ingrese nombre: ")
	if nombre=="salir" or nombre=="SALIR" or nombre=="Salir":
		print("Finalizando.....")
		break
	talla=float(input("Ingrese talla: "))
	talla_c=talla*100
	if talla<1.85:
		print("NO PROMOVIDO")
		print("Le falto:",int(185-talla_c),"cm")
	if talla>1.85:
		print("PROMOVIDO")
