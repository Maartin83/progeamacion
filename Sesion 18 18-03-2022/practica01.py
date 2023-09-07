m_0=0
me_0=0
igual_0=0
n=int(input("Cantidad de numeros a introducir: "))
for x in range(n):
	n2=int(input("Ingrese un numero:"))
	if n2>0:
		m_0+=1
	elif n2<0:
		me_0+=1
	elif n2==0:
		igual_0+=1

print("Se introdujo ",m_0," numeros mayores a 0")
print("Se introdujo ",me_0," numeros menores a 0")
print("Se introdujo ",igual_0," veces 0")