numero1 = input("Ingresar el primer número: ")
numero2 = input("Ingresar el segundo número: ")

if numero1.isnumeric() and numero2.isnumeric():
    numero1 = int(numero1)
    numero2 = int(numero2)

    operacion = input("Ingresar la operación a realizar (suma/resta/multiplicacion/division): ")

    if operacion == "suma":
        resultado = numero1 + numero2
        print("El resultado es: " + str(resultado))

    elif operacion == "resta":
        resultado = numero1 - numero2
        print("El resultado es: " + str(resultado))

    elif operacion == "multiplicacion":
        resultado = numero1 * numero2
        print(f"El resultado es: {resultado}")

    elif operacion == "division":
        resultado = numero1 / numero2
        print(f"El resultado es: {resultado}")

    else:
        print("La operación elegida no es válida.")

else:
    print("Los datos ingresados no representan números.")