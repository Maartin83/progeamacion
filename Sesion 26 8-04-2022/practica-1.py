monedas={'euro':"€",'dolar':"$",'yen':"¥"}
q=input("Ingrese tipo de moneda: ")
pregunta=q.lower()
if pregunta not in monedas:
	print(q," no se encuentra en el diccionario")
else:
	print("Simbolo: ",monedas.get(pregunta))
