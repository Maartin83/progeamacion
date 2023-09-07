maximo=0
while True:
    num=int(input())
    if num>maximo:
        maximo=num
    if num==0:
        break
print("El mayor es:",maximo)
