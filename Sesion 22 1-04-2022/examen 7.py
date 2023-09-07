lista1=[]
for x in range(5):
	n=int(input("Ingrese numero a agregar a lista: "))
	lista1.append(n)
print(lista1)
lista2=[]
lista2.extend(lista1)
lista2.reverse()
print(lista2)