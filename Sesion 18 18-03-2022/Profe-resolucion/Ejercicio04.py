v_inicial = int(input("Ingresar valor inicial: "))
v_final = int(input("Ingresar valor final: "))


for x in range(v_inicial,v_final+1):
	if x%2==0:
		print(x)