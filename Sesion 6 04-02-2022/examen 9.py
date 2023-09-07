#9. Juan, Raquel y Daniel aportan cantidades de dinero para formar un capital. Juan y Raquel aportan en dólares y Daniel, en soles.
#Desarrolle el programa que determine el capital total en dólares y que porcentaje de dicho capital aporta cada uno. Dólar = S/. 3.00 nuevos soles.
juan=float(input("Ingrese aporte de Juan:  "))
raquel=float(input("Ingrese aporte de raquel:  "))
daniel1=float(input("Ingrese aporte de daniel:  "))
daniel2=daniel1/3
capital=juan+raquel+daniel2
juanporcentaje=juan*100/capital
raquelporcentaje=raquel*100/capital
danielporcentaje=daniel2*100/capital

print("El capital total es:  ",round(capital,2))
print("El porcentaje de aporte de Juan es: {}% de Rquel es: {}% de Daniel es: {}%".format(round(juanporcentaje,2),round(raquelporcentaje,2),round(danielporcentaje,2)))
