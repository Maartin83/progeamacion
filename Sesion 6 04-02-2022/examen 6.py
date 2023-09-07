#6.Se lee un número correspondiente al radio de la circunferencia, visualizando la longitud de la misma y el área del círculo correspondiente.
#Se recuerda: AREA = PI * RADIO2 y LONGITUD = 2 * PI * RADIO
radio=int(input("Ingrese radio del circulo:  "))
area=3.14*radio**2
longitud=2*3.14*radio
print("El area del circulo es:  ",round(area,2))
print("La longitud del circulo es:  ",round(longitud,2))
