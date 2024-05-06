while True:
    num1 = int(input("Ingrese su primer número:"))
    num2 = int(input("Ingrese su primer número:"))

    try:
        division = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        print(f"Sus números divididos son igual a:{division}")

    