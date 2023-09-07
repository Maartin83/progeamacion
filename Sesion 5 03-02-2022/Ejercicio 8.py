import random
numero = int(input("Igresar numero:  "))
azar=random.randint(1,10)
print("Numero al alzar:  ",azar)
if numero==azar:
    print("felicidades le atinaste")
else:
    print("Vuelve a intentarlo")
