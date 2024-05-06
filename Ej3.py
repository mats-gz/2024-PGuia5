lista = []
indice = int(input("Ingrese el indice al cual desea acceder:"))

try:
    lista[indice]
except IndexError:
    print("Este indice no existe en la lista.")