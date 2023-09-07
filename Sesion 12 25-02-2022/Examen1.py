#Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume
numero1=float(input("Ingrese primer numero: "))
numero2=float(input("Ingrese segundo numero: "))
if numero1==numero2:
    proceso=numero1*numero2
elif numero1>numero2:
    proceso=numero1-numero2
else:proceso=numero1+numero2
print("Resultado:",proceso)
