lista_numeros = []

valor_ingresado = input("Ingrese un número natural")

while valor_ingresado != 'f':

    if valor_ingresado.isnumeric():

        lista_numeros.append(int(valor_ingresado))

    else:

        print("No se ingresó un número")
    
    valor_ingresado = input("Ingrese un número natural")

print(lista_numeros)