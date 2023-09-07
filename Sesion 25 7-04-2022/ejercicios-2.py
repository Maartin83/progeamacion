alumno={'dni':71814680,'nombre':'Jesus','apellidos':'Gonzales Pocco','distrito':'San Antonio'}
clave=['codigo','dni','distrito','edad']
for i in clave:
 	if i in alumno:
 		print(i,'----->',alumno[i])
 	else:
 		print("No esta en el diccionario: ",i)