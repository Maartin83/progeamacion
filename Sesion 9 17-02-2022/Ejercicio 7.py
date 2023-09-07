numero=int(input("Numero:  "))
d1=numero//10000
r1=numero%10000

d2=r1//1000
r2=r1%1000

d3=r2//100
r3=r2%100

d4=r3//10
d5=r3%10


suma=d1+d2+d3+d4+d5
promedio=suma/5
print("suma: ",suma)
print("inverso: ",str(d5)+str(d4)+str(d3)+str(d2)+str(d1))
