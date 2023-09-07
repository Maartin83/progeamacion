def suma(n1,n2):
	return n1+n2
def resta(n1,n2):
	return n1-n2
def multiplicacion(n1,n2):
	return n1*n2
def division(n1,n2):
	return n1/n2
n1=float(input("Ingrese primer valor: "))
n2=float(input("Ingrese segundo valor: "))

print("Suma: ",round(suma(n1,n2),1))
print("Resta: ",round(resta(n1,n2),1))
print("multiplicacion: ",round(multiplicacion(n1,n2),1))
print("division: ",round(division(n1,n2),1))