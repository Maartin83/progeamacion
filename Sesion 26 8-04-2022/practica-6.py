def login():
	c=1
	while c<=3:
		user=input("Ingrese nombre de usuario: ")
		contra=input("ingrese contraseña: ")
		user=str(user)
		contra=str(contra)
		if c>=4:
			break
		if user=="usuario1" and contra=="123456":
			print("Acceso Correcto")
		else:
			print("Acceso Denegado")
		c+=1
login()
