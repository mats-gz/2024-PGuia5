try:
    numero = int(input("Ingrese un número:"))
except ValueError:
    print("El valor ingresado no es válido.")
else:
    print("Su número es:", numero)