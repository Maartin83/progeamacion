lista=[]
num=int(input("Ingrese numero a multiplicar: "))
for x in range(1,13):
	mult=x*num
	lista.append(mult)
	print(x," x ",num," = ",mult)
print("Guardando resultados en lista...")
print(lista)