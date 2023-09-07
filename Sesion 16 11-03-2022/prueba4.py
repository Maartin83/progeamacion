minimo=9999999999
while True:
    num=int(input())
    if num<minimo and num!=0:
        minimo=num
    if num==0:
        break
print("El menor es:",minimo)
