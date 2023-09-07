lista1=[]
lista2=[]
lista3=[]
for x in range(5):
	n1=int(input("Ingrese numero para lista nro 1: "))
	lista1.append(n1)
print("--------------------------------------------------")
for y in range(5):
	n2=int(input("Ingrese numero para lista nro 2: "))
	lista2.append(n2)
lista3=lista1+lista2
print("Lista 1 :",lista1)
print("Lista 2 :",lista2)
print("Lista 3 :",lista3)