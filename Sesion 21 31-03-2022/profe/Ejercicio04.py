#Ingresar valores numeros en una lista, el ingreso de numeros terminara cuando se 
#escriba el 0.

lista=[]

valor = int(input("ingresar valor (0 para finalizar): "))

while valor != 0:
	lista.append(valor)
	valor = int(input("ingresar valor (0 para finalizar): "))

print(lista)
print("Cantidad de elementos:",len(lista))