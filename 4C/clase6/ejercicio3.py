lista_palabras = []

while True:
    palabra = input("Ingrese una palabra (o 'fin' para finalizar): ")

    if palabra == 'fin':
        break

    else:
        lista_palabras.append(palabra)

contador_hola = 0

for palabra in lista_palabras:
    if palabra == 'hola':
        contador_hola += 1

print(f'La cantidad de veces que se ingresó "hola" es: {contador_hola}')