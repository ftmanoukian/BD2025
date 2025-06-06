mi_lista_ejemplo = [1,'a',[7,8,9],'hola',57.3]
print(f'lista completa: {mi_lista_ejemplo}')

# extraigo de a un elemento:
primer_elem = mi_lista_ejemplo[0]
ultimo_elem = mi_lista_ejemplo[-1]

print(f'primer_elem: {primer_elem}')
print(f'ultimo_elem: {ultimo_elem}')

#extraigo múltiples elementos
primeros_2_elem = mi_lista_ejemplo[0:2]
print(f'primeros_2_elem: {primeros_2_elem}')

prueba_2_elem = mi_lista_ejemplo[1:2]
print(f'prueba_2_elem: {prueba_2_elem}')

prueba_ord_inverso = mi_lista_ejemplo[2:0]
print(f'prueba_ord_inverso: {prueba_ord_inverso}')

prueba_limites = mi_lista_ejemplo[0:183]
print(f'prueba_limites: {prueba_limites}') 
#si pongo un índice de fin mayor que el máximo índice posible, 
# se queda con todos los elementos hasta el final del conjunto