asignaturas={'Matemáticas': 6, 'Física': 4, 'Química': 5}
print("Matemáticas tiene:",asignaturas.get('Matemáticas'),"creditos")
print("Fisica tiene:",asignaturas.get('Física'),"creditos")
print("Quimica tiene:",asignaturas.get('Química'),"creditos")
print(    )
print("Creditos en total:",asignaturas.get('Matemáticas')+asignaturas.get('Física')+asignaturas.get('Química'))