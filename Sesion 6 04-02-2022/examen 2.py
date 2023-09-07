#2.Un alumno desea saber cuál será su calificación final en la materia de Lógica Computacional.
#Dicha calificación se compone de tres exámenes parciales cuya ponderación es de 30%, 30% y 40%.
c1=float(input("Ingrese primera calificacion:  "))
c2=float(input("Ingrese segunda calificacion:  "))
c3=float(input("Ingrese tercera calificacion:  "))
promedio=(c1+c2+c3)/3
examen1=promedio*0.30
examen2=promedio*0.30
examen3=promedio*0.40
calificacionfinal=examen1+examen2+examen3
print("Calificacion final:  ",round(calificacionfinal,2))
