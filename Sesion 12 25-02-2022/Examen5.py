"""En una tienda de descuento se efectúa una promoción
en la cual se hace un descuento sobre el valor de la compra total según el color de la bolita que el cliente saque al pagar en caja.
Si la bolita es de color blanco no se le hará descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un 25%,
si es azul un 50% y si es roja un 100%.
Determinar la cantidad final que el cliente deberá pagar por su compra se sabe que solo hay bolitas de los colores mencionados."""
monto=float(input("Ingrese monto a pagar: "))
bolitax=input("Ingrese color de bolita de descuento: ")
bolita=bolitax.lower()
if bolita=="blanco":
    desc=0
elif bolita=="verde":
    desc=0.10*monto
elif bolita=="amarrilla":
    desc=0.25*monto
elif bolita=="azul":
    desc=0.50*monto
elif bolita=="rojo":
    desc=1*monto
print("Tu descuento es de:",desc)
print("Total a pagar:",monto-desc)
