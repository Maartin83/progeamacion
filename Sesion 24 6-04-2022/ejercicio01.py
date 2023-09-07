def validar(email):
	for c in email:
		if c =="@":
			return True
	return False
dirreccion=input("Ingrese Dirrecion email: ")
if validar(dirreccion):
	print("Dirrecion email valida")
else:
	print("Dirrecion email no valida")