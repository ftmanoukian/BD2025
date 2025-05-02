"""
Solicitar al usuario su año de nacimiento.
Si el año ingresado no es válido, se debe solicitar nuevamente hasta que lo sea.
Caso contrario, se debe informar si puede ingresar a un evento para mayores de 15 años.
"""

año_nacimiento = input("Ingrese su año de nacimiento: ")

while not (año_nacimiento.isnumeric() and int(año_nacimiento) <= 2025 and int(año_nacimiento) >= 1925):
    print("El dato ingresado no es válido")
    año_nacimiento = input("Ingrese su año de nacimiento: ")

edad = 2025 - int(año_nacimiento)

if edad >= 15:
    print("Puede ingresar al evento")
else:
    print("No puede ingresar al evento")