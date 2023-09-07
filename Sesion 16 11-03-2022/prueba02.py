c=1
suma=0
x=0
while c<=10:
    numero=int(input())
    if numero>=0:
        suma=suma+numero
        x=x+1
    else:
        print("Programa finalizado por numero negativo")
        break
    c=c+1
prom=suma/x
print("Promedio:",prom)
