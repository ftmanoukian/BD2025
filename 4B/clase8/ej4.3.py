continuar_ingreso = True
lista_notas = []

while continuar_ingreso:

    ingreso_usuario = input("Ingrese una nota (o 'fin' para finalizar): ")

    if ingreso_usuario == 'fin':
        continuar_ingreso = False
    else:
        if ingreso_usuario.isnumeric():
            lista_notas.append(int(ingreso_usuario))

suma = sum(lista_notas)
cant = len(lista_notas)
prom = suma / cant

print(f'Promedio: {prom}')