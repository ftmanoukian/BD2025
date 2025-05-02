lista_numeros = []

while True:
    valor_ingresado = input("Ingrese un número natural: ")

    if valor_ingresado.isnumeric():
        lista_numeros.append(int(valor_ingresado))
    
    elif valor_ingresado == 'f':
        break
    
    else:
        print("El valor ingresado NO es válido")

acumulador = 0

for valor in lista_numeros:
    acumulador += valor

print(f'El resultado de la suma es {acumulador}')
