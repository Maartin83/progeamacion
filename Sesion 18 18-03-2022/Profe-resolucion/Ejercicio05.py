while True:
	caracter = input("Ingresar caracter: ")
	#if caracter =='a' or caracter =='e' or caracter =='i' or caracter =='o' or caracter =='u':
	if caracter in ('a','e','i','o','u'):
		print("VOCAL")
	else:
		print("NO VOCAL")

	if caracter == " ":
		break
print("Ingreso detenido por un espacio en Blanco...")