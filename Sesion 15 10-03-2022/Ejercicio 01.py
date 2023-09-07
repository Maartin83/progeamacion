c=1
x=0
suma=0
prom=0
while c<=10:
    num=int(input())
    if num >=0:
        suma=suma+num
        x=x+1
    else :
        print("Programa Finalizado por el numero negativo")
        break
prom=suma/x
print("Promedio: ",round(prom,2))
