num1 = input("Ingresar el primer número: ")
num2 = input("Ingresar el segundo número: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)

    operacion = input("Ingrese una operación (suma/resta/multiplicacion/division)")

    if operacion == "suma":
        resultado = num1 + num2

        print(f"El resultado es {resultado}")

    elif operacion == "resta":
        resultado = num1 - num2
        
        print(f"El resultado es: {resultado}")

    elif operacion == "multiplicacion":
        resultado = num1 * num2

        print(f"El resultado es: {resultado}")        

    elif operacion == "division":
        if num2 != 0:
            resultado = num1 / num2

            print(f"El resultado es: {resultado}")
        
        else:
            print("No se puede realizar una división por cero")

    else:
        print("Operación no válida")

else:
    print("Al menos uno de los números no es válido.")