###El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas.
###Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera  práctica calificada,
###si es que esta no es menor que 10.
###Desarrolle el programa que determine el promedio final de un alumno conociendo sus tres notas
n1=float(input("Ingrese primera nota:  "))
n2=float(input("Ingrese segunda nota:  "))
n3=float(input("Ingrese tercera nota:  "))
promedio=(n1+n2+n3)/3
if promedio>=10:
    nf=promedio+2
    print("El promedio final del alumno es:  ",round(nf,1))
else:
    print("El promedio final del alumno es:  ",round(promedio,1))
    
