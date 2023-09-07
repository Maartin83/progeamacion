"""Se tiene que evaluar cuatro notas de un alumno, como resultado se visualiza el promedio del alumno junto con su condición de APROBADO o DESAPROBADO, si
este aprobado y con 18 o más, saldrá el siguiente mensaje “Certificado en MSOFFICE” """
nota1=float(input("Ingresar primera nota: "))
nota2=float(input("Ingresar segunda nota: "))
nota3=float(input("Ingresar tercera nota: "))
nota4=float(input("Ingresar cuarta nota: "))
promedio=(nota1+nota2+nota3+nota4)/4
print("Promedio:",round(promedio,1))
if promedio>=18:
    print("APROBADO")
    print("***********************")
    print("Certificado en MSOFFICE")
    print("***********************")
elif promedio>=14:
    print("APROBADO")
else:print("DESAPROBADO")
