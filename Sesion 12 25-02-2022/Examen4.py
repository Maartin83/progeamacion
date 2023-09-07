"""Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
sabiendo que cuando las horas de trabajo no exceden de 40,
el resto se consideran horas extras y que estas se pagan al doble de una hora normal cuando no exceden de 8;
si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se pagan las horas normales y el resto al triple"""
preciodeh=float(input("Ingrese el precio por horas trabajadas: "))
horas=int(input("Ingresar horas trabajadas: "))
if horas>40 and horas<=48:
    pagodoble=(48-horas)*(preciodeh*2)
    pago=pagodoble
elif horas>48:
    horadoble=8*(preciodeh*2)
    horatriple=(horas-48)*(preciodeh*3)
    pago=horadoble+horatriple
print("Pago por concepto de horas extras es: ",pago)
