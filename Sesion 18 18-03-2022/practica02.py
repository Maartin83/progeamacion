n_caracter=int(input("Ingrese numero de veces a ingresar: "))

for x in range(n_caracter):
	caracter=input("Ingrese caracter: ")
	if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
		print("VOCAL")
	elif caracter==" ":
		print("Ningun caracter identificado, finalizando...")
		break
	else:
		print("NO VOCAL")