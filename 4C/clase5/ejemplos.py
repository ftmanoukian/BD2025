mi_lista_ejemplar = ["hola",7,24.4732,'s']

print(mi_lista_ejemplar[0])         # primer elemento
print(mi_lista_ejemplar[3])         # último elemento

print(mi_lista_ejemplar[-1])        # último elemento, utilizando índice negativo

mi_lista_ejemplar[0] = 'chau'       # modifico el primer elemento
print(mi_lista_ejemplar)

# creo una segunda lista, y la agrego a la primera utilizando "append"
mi_lista_ejemplar2 = ["arbol","perro","pipsa","tren","avion","barco"]
mi_lista_ejemplar.append(mi_lista_ejemplar2)
print(mi_lista_ejemplar)
print(mi_lista_ejemplar[-1])

# deshago el cambio anterior *removiendo* el ultimo elemento con pop()
# agrego la segunda lista a la primera utilizando extend()
mi_lista_ejemplar.pop()
mi_lista_ejemplar.extend(mi_lista_ejemplar2)
print(mi_lista_ejemplar)