#Metodos de las Listas
alumnos =['A001','Javier Perez',32,3500,'Comas']
#Mostrar todos los datos de la lista
print(alumnos[:])
#Agregar elemento a la lista en la ultima posicion
alumnos.append('Masculino')
print(alumnos[:])
#Agregar elemento a la lista en una posicion especifica
alumnos.insert(2,'Sistemas')
print(alumnos[:])
#Cantidad de elementos de la lista
print("Cantidad de elementos:",len(alumnos))
#Eliminar un elemento de la lista
alumnos.remove('Comas')
print(alumnos[:])
#Obtener la posicion de un elemento
print("La posicion del nombre del alumno:",alumnos.index('Javier Perez')+1)
#Invertir los elementos de la lista
alumnos.reverse()
print(alumnos[:])
#Eliminar el ultimo elemento
alumnos.reverse()
alumnos.pop()
print(alumnos[:])
#Eliminar todos los elementos de la lista
alumnos.clear()
print(alumnos)