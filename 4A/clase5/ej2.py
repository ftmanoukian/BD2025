"""
Solicitar al usuario su año de nacimiento. Verificar que el dato ingresado represente un año válido, y en caso contrario volver a solicitarlo. Luego, calcular la edad. En caso de que el usuario sea mayor de 18 años, informar que puede ingresar a la fiesta. Caso contrario, informar que no puede hacerlo.
"""

año = input("Ingrese su año de nacimiento: ")

while not (año.isnumeric() and 1925 <= int(año) <= 2025):
    print("El año ingresado no representa un número válido.")
    año = input("Ingrese su año de nacimiento: ")

edad = 2025 - int(año)

if edad >= 18:
    print("Puede ingresar a la fiesta")
else:
    print("No puede ingresar a la fiesta")