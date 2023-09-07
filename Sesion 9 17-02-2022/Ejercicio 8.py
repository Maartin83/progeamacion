horas=int(input("Horas Trabajadas:  "))
if horas <=40:
    salario=horas*16
    print("Salario:  ",salario)
else:
    dif=horas-40
    salariobase=40*16
    extra=dif*20
    salariofinal=salariobase+extra
    print("Salario Base:  ",salariobase)
    print("Horas Extra:  ",extra)
    print("Salario:  ",salariofinal)
