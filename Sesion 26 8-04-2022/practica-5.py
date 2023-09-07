dni=int(input("Ingrese DNI: "))
def validar(dni):
	dni=str(dni)
	if len(dni)==8:
		print("DNI Correcto: ")
	else:
		print("DNI Incorrecto")
validar(dni)
