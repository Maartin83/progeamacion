import random
c=1
par=0
inpar=0
suma_t=0
suma_par=0
suma_inpar=0
mayor=0
menor=9999
numero=0
while c<=50:
	numero=random.randint(1,1000)
	print(numero)
	suma_t+=numero
	c+=1
	if numero%2==0:
		par+=1
		suma_par+=numero
	if numero%2!=0:
		inpar+=1
		suma_inpar+=numero
	if numero > mayor:
		mayor=numero
	if numero<menor:
		menor=numero
print("******************************")
print("hay ",par," numeros pares")
print("hay ",inpar," numeros inpares")
print("La suma total es: ",suma_t)
print("La suma de los pares es: ",suma_par)
print("La suma de los inpares es: ",suma_inpar)
print("El numero mayor es: ",mayor)
print("El numero menor es: ",menor)
	