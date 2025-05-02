print("Validador de nombres de usuario.")
print(" - Debe tener entre 3 y 12 caracteres")
print(" - No debe contener espacios")
print(" - No debe ser completamente numérico")

nombre_usuario = input("Ingrese un nombre de usuario: ")

hay_espacios = False

for caracter in nombre_usuario:

    if caracter.isspace():
        hay_espacios = True

if (not hay_espacios) and (not nombre_usuario.isnumeric()) and (len(nombre_usuario) >= 3 and len(nombre_usuario) <= 12):
    print("La contraseña es válida")
else:
    print("La contraseña NO es válida")
