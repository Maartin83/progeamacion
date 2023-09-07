#Calcular la bonificacion de un empleado en funcion a sueldo Basico;
#Si el Sueldo >=3000 : 2%
#Si el sueldo >=2000 : 5%
#Si el sueldo <2000 : 10%

s_basico = float(input("Ingresar Sueldo Basico: "))

if s_basico >= 3000:
    bonif = s_basico * 0.02
elif s_basico >= 2000:
    bonif = s_basico * 0.05
else:
    bonif = s_basico * 0.10
    
s_final = s_basico + bonif

print("Bonificacion:",bonif)
print("Sueldo Final:",s_final)
