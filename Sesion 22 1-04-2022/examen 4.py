lista=[]
while True:
	n=int(input("Ingrese numero a agregar(Ingrese 0 para detener): "))
	if n==0 :
		break
		print("Finalizando....")
	lista.append(n)
lista.sort()
print (lista)