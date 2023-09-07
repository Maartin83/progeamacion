n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1+n2+n3)/3

print("Promedio:",round(promedio))

if promedio > 18 :
 print("Aprobado y Excelente")
elif promedio >= 12.5:
 print("Aprobado")
else:
 print("Desaprobado")
