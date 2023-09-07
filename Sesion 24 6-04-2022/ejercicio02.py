def primo(numero):
	for x in range(2,numero):
		if numero%x==0:
			return False
	return True
while True:
	num=int(input("Ingrese numero: "))
	if primo(num)==True:
		print("Es primo")
	else:
		print("No es primo")