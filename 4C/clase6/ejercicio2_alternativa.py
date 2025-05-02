lista_numeros_pares = []
lista_numeros_impares = []

while True:
    valor_ingresado = input("Ingrese un número natural: ")

    if valor_ingresado.isnumeric() and int(valor_ingresado) % 2 == 0:
        lista_numeros_pares.append(int(valor_ingresado))

    elif valor_ingresado.isnumeric() and int(valor_ingresado) % 2 != 0:
        lista_numeros_impares.append(int(valor_ingresado))
    
    elif valor_ingresado == 'f':
        break
    
    else:
        print("El valor ingresado NO es válido")

acumulador_pares = 0

for valor in lista_numeros_pares:
    acumulador_pares += valor

print(f'El resultado de la suma de numeros pares es {acumulador_pares}')

acumulador_impares = 0

for valor in lista_numeros_impares:
    acumulador_impares += valor

print(f'El resultado de la suma de numeros impares es {acumulador_impares}')
