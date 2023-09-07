s_bruto = float(input("Sueldo bruto:  "))
descuento = float(input("Descuento:  "))
impuesto = s_bruto*0.08
afp = s_bruto*0.13
sueldo_neto = s_bruto-impuesto-afp-descuento
print("Impuesto:  ",impuesto)
print("AFP:  ",afp)
print("Sueldo neto:  ",sueldo_neto)
