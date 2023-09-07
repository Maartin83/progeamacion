valor1 = input("nombre del trabajador:  ")
valor2 = float(input("Horas trabajadas:  "))
valor3 = float(input("Precio de cobra por hora:  "))
total = valor2 * valor3
valor4 = 0.10 * total
final = total - valor4

print("REPORTE DE PAGOS")
print("-"*15)
print("Nombre dle trabajador:  ",valor1)      
print("Sueldo bruto:  ",total)
print("Descuento de la renta:  ",valor4)
print("Salario a pagar:  ",final)
