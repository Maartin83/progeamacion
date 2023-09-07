###Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
###El que está detrás viaja a una velocidad mayor.
###Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h)
###y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
distancia=float(input("Ingresar distancia entre los dos vehiculos en km:  "))
velo1=float(input("Ingresar velocidad del vehivulo 1 en kmh:  "))
velo2=float(input("Ingresar velocidad del vehivulo 2 en kmh:  "))
diferenciavelocidad = velo1-velo2
tiempo = distancia / diferenciavelocidad
tiempomin=tiempo*60
print("El tiempo en el que alcanzara el vehiculo mas rapido al otro es de:  ",round(tiempomin,2))
