precios={'platano':0.50,'manzana':0.65,'melocoton':0.85,'pera':1.0}
fruta=input("Ingrese Fruta: ")
cantidad=int(input("Ingrese cantidad a comprar: "))
if fruta not in precios:
	print("La fruta no se encuentra en el diccionario")
else:
	print("El precio de",cantidad,fruta+"s","es:",cantidad*precios.get(fruta))