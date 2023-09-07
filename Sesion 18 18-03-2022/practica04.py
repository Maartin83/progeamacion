incio=int(input("ingrese numero donde comenzara: "))
final=int(input("ingrese numero donde terminara: "))
print("Los numeros pares desde",incio," hasta ",final," son:")
for x in range(incio+1,final-1):
	if x%2==0:
		print(x," ",end="")