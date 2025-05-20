lista_origen = ['Matilde','Jose','Juan','Jose','Martin','Ailen']
lista_destino = []

for elemento_origen in lista_origen:
    
    esta_repetido = False

    for elemento_destino in lista_destino:
        
        if elemento_origen == elemento_destino:
            
            esta_repetido = True

    if esta_repetido == False:
        
        lista_destino.append(elemento_origen)

print(lista_origen)
print(lista_destino)