c_m=0 
c_f=0 
c_mayores=0 
c_menores=0

for x in range(5):
	print("*****************:")
	nombre=input("Nombre: ")
	sexo=input("Sexo(F o M without space): ")
	edad=int(input("Edad: "))
	if sexo=="M":
		c_m+=1
	else:
		c_f+=1
	if edad>=18:
		c_mayores+=1
	else : 
		c_menores+=1

print("Cantidad de masculino:",c_m)
print("Cantidad de femenimo:",c_f)
print("Cantidad de mayores de edad:",c_mayores)
print("Cantidad de menores de edad:",c_menores)