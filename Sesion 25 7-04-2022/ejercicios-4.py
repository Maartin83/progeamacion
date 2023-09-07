alumno = {'dni':42994068,'nombre':'Eder','apellidos':'Ortiz Camacho','distrito':'Independencia'}
#get(): Devuelve el valor que corresponde con Key introducida
print(alumno.get('dni'))
#pop(): Devuelve el valor que corresponde con la Key introducida y luego lo elimina.
print(alumno.pop('distrito'))
print(alumno)
#update(): Actualiza el valor de un determinado Key o lo crea si no existe.
alumno.update({'nombre':'Maria'})
alumno.update({'edad':36})
print(alumno)