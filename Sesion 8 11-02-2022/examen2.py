###Un alumno desea saber cuál será su calificación final en la materia de Lógica Computacional.
###Dicha calificación se compone de tres exámenes parciales cuya ponderación es de 30%, 30% y 40%
v1=float(input("Ingrese nota del primer examen:  "))
v2=float(input("Ingrese nota del segundo examen:  "))
v3=float(input("Ingrese nota del tercer examen:  "))
promedio=(v1+v2+v3)/3
examen1=promedio*0.30
examen2=promedio*0.30
examen3=promedio*0.40
calificacionf=examen1+examen2+examen3
print("La calificaion final es de:  ",round(calificacionf,2))
