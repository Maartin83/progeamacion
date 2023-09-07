n=int(input("Ingrese numero : "))
m=int(input("Ingrese numero de multiplos: "))
multiplos=[]
for i in range(m):
	mult=n*(i+1)
	multiplos.append(mult)
print(multiplos)
	
