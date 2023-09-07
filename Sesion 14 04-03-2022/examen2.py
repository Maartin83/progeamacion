examen_escrito=float(input("Ingrese nota del examen escrito: "))
lecciones=float(input("Ingrese nota de lecciones: "))
tareas=float(input("Ingrese nota de tareas: "))
laboratorio=float(input("Ingrese nota del laboratorio: "))
v1=examen_escrito/5
v2=lecciones*2
v3=tareas*2
v4=laboratorio*2
v1p=v1*0.60
v2p=v2*0.20
v3p=v3*0.15
v4p=v4*0.05
pf=v1p+v2p+v3p+v4p

print("Calificacion FInal:",pf)

