#Definir una lista vacia y luego solicitar la cargar de 5 numeros enteros ingresados por
#teclado. Imprimir la lista generada.

lista = []

for i in range(5):
	valor = int(input("Ingrese valor entero "+str(i+1)+": "))
	lista.append(valor)

print("Lista de numeros enteros")
print(lista)