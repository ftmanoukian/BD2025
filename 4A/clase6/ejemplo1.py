profes_meca = ['Agus','Eze','Marcos','Manu','Ayax']

print(f'Lista original: {profes_meca}')

profes_meca.append('Fran')

print("Lista luego de utilizar append('Fran'):")
print(profes_meca)

profes_meca.insert(2,'Mechi')

print("Lista luego de insert(2,'Mechi')")
print(profes_meca)

profes_meca2 = ['Facu','Ale','Mirko','Juanse']
profes_meca.extend(profes_meca2)

print("Lista después de extend(profes_meca2)")
print(profes_meca)

profes_meca.remove('Manu')

print("Lista después de remove('Manu')")
print(profes_meca)

profes_meca.pop(7)

print("Lista después de pop('7')")
print(profes_meca)

profes_meca.sort()

print("Lista después de sort()")
print(profes_meca)

profes_meca.sort(reverse=True)

print("Lista después de sort(reverse=True)")
print(profes_meca)

indice_ayax = profes_meca.index('Ayax')

print("Indice de 'Ayax':")
print(indice_ayax)

cantidad_profes = len(profes_meca)

print("Cantidad de elementos de profes_meca")
print(cantidad_profes)