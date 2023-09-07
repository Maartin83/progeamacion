###Un estudiante recibe una propina mensual S/. 20.
###El estudiante rinde mensualmente dos exámenes.
###Su papá ha decidido incentivarlo dándole una propina adicional de S/. 5 por cada examen aprobado.
###Desarrolle el programa que determine el monto total de la propina.
valor1=int(input("Examenes aprobados:  "))
if valor1==2:
    propina=30
else:propina=25
if valor1==0:
    propina=20
print("La propina total es:",propina,"soles")
