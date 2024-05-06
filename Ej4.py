def operacion_numeros(num1, num2):
    suma = num1 + num2
    resta = num1 - num2

    return print(f"Los resultados son:{suma}, {resta}")

try:
    operacion_numeros(5, "1")
except TypeError:
    print("Los valores ingresados no son numéricos, intente devuelta.")