#Crear una lista que almacene "n" numeros multiplos de un numero numero entero.
#Muestre los valores de la lista.

multiplos=[]

cantidad = int(input("Ingresar Cantidad de Multiplos: "))
numero = int(input("Ingresar numero entero: "))

for x in range(cantidad):
	m = numero * (x+1)
	multiplos.append(m)

print("Los ", cantidad," multiplos de ",numero," son:")
print(multiplos)

