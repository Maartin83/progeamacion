alumno={'dni':71814680,'nombre':'Jesus','apellidos':'Gonzales Pocco','distrito':'San Antonio'}

for x in alumno.keys():
	print(x,'----->',alumno[x])
print(  )
print(  )
for clave,valor in alumno.items():
	print(clave,'------>',valor)
print(  )
print(  )
print('Mostrando solo valores del diccionario')
print(  )
for x in alumno.values():
	print(x)