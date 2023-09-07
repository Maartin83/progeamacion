#Ingresar el nombre y peso de personas, hasta que el peso sea un numero negativo y sea mayor
#a 190 kg.

cont = 0
peso = 1

while peso > 0 and peso <= 190:
	nombre = input("Nombre: ")
	peso = int(input("Peso: "))
	cont += 1

print("Personas registradas:",cont-1) 
