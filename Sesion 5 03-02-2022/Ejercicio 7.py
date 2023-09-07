#Crear un algoritmo que genera 4 numeros aleatorios, luego
#mostrar el mayor y menor de ellos.
import random

n1=random.randint(1,100)
n2=random.randint(1,100)
n3=random.randint(1,100)
n4=random.randint(1,100)

print("los numeros son: {} - {} - {} - {}".format(n1,n2,n3,n4))

mayor=max(n1,n2,n3,n4)
menor=min(n1,n2,n3,n4)

print("El mayor es: {} y el menor es: {}".format(mayor,menor))
