c=1
suma=0
while c<=10:
    num=int(input())
    if num%2==0:
        suma=suma+num
    if num==0:
        break

print("Suma de los numeros pares:",suma)
