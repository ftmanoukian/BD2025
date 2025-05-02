año = input("Ingrese su año de nacimiento: ")

while not(año.isnumeric() and int(año) < 2025 and int(año) > 1925):
    año = input("Año no válido. Ingresar nuevamente:")

edad = 2025 - int(año)

if edad >= 15:
    print("Puede ingresar")
else:
    print("No puede ingresar")