"""Determine el tiempo de servicio de acuerdo con el año de ingreso. Si el trabajador tiene
menos de 4 años el tendrá un aumento del 15% de su sueldo básico, en caso contrario
tendrá un aumento del 12% por cada año. Muestre el Monto a Cobrar"""
ingreso=int(input("Ingrese año de ingreso: "))
sueldo=float(input("Ingrese monto de sueldo: "))
tiempo=2022-ingreso
if tiempo<4:
    aumento=0.15*sueldo
else: aumento=tiempo*(sueldo*0.12)
montof=sueldo+aumento
print("años de servicio:",tiempo)
print("Aumento:",aumento)
print("Monto total a cobrar:",montof)
