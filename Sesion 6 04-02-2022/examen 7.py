#7.Desarrolle el programa que determine el área y el perímetro de un rectángulo
#sabiendo que el   área = b x h, perímetro = 2x (b+h).
base=float(input("Ingresar base del rectangulo:  "))
altura=float(input("Ingresar altura del rectangulo:  "))
area=base*altura
perimetro=2*(base+altura)
print("El perimetro del rectangulo es: {} y el area es {} ".format(perimetro,area))
