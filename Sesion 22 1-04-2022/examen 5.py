lista=[]
suma=0 ; 
for x in range(10):
	n=int(input("Ingrese numero: "))
	lista.append(n)
	suma+=n
print(lista)
print("La suma de los numeros de la lista es: ",suma)
print("El promedio de los numeros de la lista es: ",suma/10)