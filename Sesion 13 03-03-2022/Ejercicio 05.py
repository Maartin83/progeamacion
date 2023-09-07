c = 1
c_m = 0
c_f = 0
mayor = 0
menor = 0

while c <= 5:
 print("***********************************")   
 nombre = input("Nombre: ")
 apellido = input("Apellidos: ")
 sexo = input("Sexo: ")
 edad = int(input("Edad: "))
 print("***********************************")
 if sexo == "M":
  c_m = c_m + 1
 else:
  c_f = c_f + 1

 if edad >= 18:
  mayor = mayor + 1
 else:
  menor = menor + 1
 c = c + 1

print("***********************************")
print("Cantidad de Varones:",c_m)
print("Cantidad de Mujeres:",c_f)
print("Cantidad de Mayores de edad:",mayor)
print("Cantidad de Menores de edad:",menor)
print("***********************************")
