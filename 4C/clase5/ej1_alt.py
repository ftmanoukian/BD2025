lista_numeros = []

while True:

    valor_ingresado = input("Ingrese un valor numérico: ")

    if valor_ingresado == 'f':
        break

    if valor_ingresado.isnumeric():
        lista_numeros.append(int(valor_ingresado))

    else:
        print("El valor ingresado no representa un número")

print(lista_numeros)