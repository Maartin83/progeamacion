numero = int(input("Ingrese numero:  "))

d1=numero//1000
r1=numero%1000

d2=r1//100
r2=r1%100

d3=r2//10
d4=r2%10

rv=d4*1000+d3*100+d2*10+d1
print("el numero en reversa es:  ",rv)
