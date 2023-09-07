reverso=0
num = int(input("Numero positivo: "))
while num != 0:
 digito = num%10
 cantidad =len(str(num))
 x=(10**(cantidad-1))*digito
 reverso=reverso+x
 
 num = num // 10
print("Numero alrevez:",reverso)