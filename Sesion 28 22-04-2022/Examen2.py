turno=input("Ingrese turno: ")
turnom=turno.lower()
afp=input("Ingrese Afp: ")
afpm=afp.lower()
sueldobasico=float(input("Ingresar sueldo basico:"))

def bono(turnom):
	if turnom=="mañana":
		bono=50
	if turnom=="tarde":
		bono=80
	if turnom=="noche":
		bono=100
	return(bono)
def descuento(afpm,sueldobasico):
	if afpm=="integra":
		descuento=sueldobasico*0.10
	if afpm=="union":
		descuento=sueldobasico*0.08
	if afpm=="vida":
		descuento=sueldobasico*0.06
	if afpm=="prima":
		descuento=sueldobasico*0.04
	if afpm=="horizonte":
		descuento=sueldobasico*0.02
	return(descuento)
print("*********************************")
print("El Bono es de:",bono(turnom))
print("El Descuento es de:",descuento(afpm,sueldobasico))
print("El Sueldo Neto es de:",bono(turnom)+sueldobasico-descuento(afpm,sueldobasico))
print("*********************************")