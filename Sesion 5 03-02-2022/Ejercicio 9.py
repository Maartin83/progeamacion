import random
numero=random.randint(100,999)
print("numero:  ",numero)

d1=numero//100
res=numero%100

d2=res //10
d3=res%10

suma =d1+d2+d3
print("La suma de os digitos es:  ",suma)
