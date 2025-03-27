# Hacer un programa que pregunte al usuario su año de nacimiento
# y le responda si puede entrar a una fiesta para gente mayor
# de edad.


año = input("Ingresá tu año de nacimiento: ")

if año.isnumeric():

    edad = 2025 - int(año)

    if edad >= 18:

        print("Podés ingresar a la fiesta")

    else:

        print("no podés ingresar a la fiesta")

else:

    print("No ingresaste un año válido")