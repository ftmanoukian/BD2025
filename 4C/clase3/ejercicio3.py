año_nacimiento = input("¿En qué año naciste? ")

if año_nacimiento.isnumeric():
    edad = 2025 - int(año_nacimiento)
    if edad >= 18:
        print("Podés ingresar a la fiesta")
    else:
        print("No podés ingresar")
else:
    print("El dato ingresado no es válido")

print("Programa hecho por 4C meca")