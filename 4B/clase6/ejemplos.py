profes_meca = ['manu','mechi','ailu','ayax','eze','facu']

print("Lista de profes:")
print(profes_meca)

profes_meca[0] = 'fran'

print("Lista después de hacer: profes_meca[0] = 'fran'")
print(profes_meca)

profes_meca.append('manu')

print("Lista después de hacer: profes_meca.append('manu')")
print(profes_meca)

profes_meca.insert(3,'agus')

print("Lista después de hacer: profes_meca.insert(3,'agus')")
print(profes_meca)

profes_meca2 = ['ruben','ale','mirko','lean']
profes_meca.extend(profes_meca2)

print("Lista después de hacer: profes_meca.extend(profes_meca2)")
print(profes_meca)

profes_meca.remove('manu')

print("Lista después de hacer: profes_meca.remove('manu')")
print(profes_meca)

profes_meca.pop(3)

print("Lista después de hacer: profes_meca.pop(3)")
print(profes_meca)

profes_meca.sort()

print("Lista después de hacer: profes_meca.sort()")
print(profes_meca)

profes_meca.sort(reverse = True)

print("Lista después de hacer: profes_meca.sort()")
print(profes_meca)

print("len(profes_meca):")
print(len(profes_meca))