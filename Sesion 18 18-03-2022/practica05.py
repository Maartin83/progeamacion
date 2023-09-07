base=float(input("ingrese numero base: "))
exponente=int(input("ingrese numero exponencial: "))
c=base
for x in range(1,exponente):
 	c=c*base
print(c)