c = 1
c_lince = 0
c_Breña = 0
c_SMiguel = 0

while c <= 10:
 distrito = input("Ingresar distrito: ")
 if distrito == 'Lince':
  c_lince = c_lince + 1
 elif distrito == 'Breña':
  c_Breña = c_Breña + 1
 elif distrito == 'San miguel':
  c_SMiguel = c_SMiguel + 1

 c = c + 1

print("Cantidad de Lince:",c_lince)
print("Cantidad de Breña:",c_Breña)
print("Cantidad de San miguel:",c_SMiguel)
