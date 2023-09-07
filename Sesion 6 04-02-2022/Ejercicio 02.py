#Calcular el salario de un trabajo en funcion a las horas trabajdas y al
#costo por hora; ademas de otorgarle una bonnificacion del 10% del salario
#si el salario es menor a 1000 soles obtener el salario final
hora = float(input("Ingresesar horas trabajadas;  "))
cxh=float(input("Inegresar costo por hora:  "))

salario=hora*cxh

if salario<1000:
    bonificacion=salario*0.10
else:
    bonificacion=0
salariofinal= salario+bonificacion
print("Salario base:  ",salario)
print("Bonificacion:  ",bonificacion)
print("Salario Final:  ",salariofinal)

   
