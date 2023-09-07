lista=[]
valor=int(input("ingresar valor(0 para finalizar): "))
while valor !=0:
	lista.append(valor)
	valor=int(input("ingresar valor(0 para finalizar): "))
print(lista)
print("cantidad de elementos:",len(lista))