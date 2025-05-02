num1 = input("Ingresar el primer número: ")
while not num1.isnumeric():
    print("Primer número ingresado no válido")
    num1 = input("Ingresar el primer número: ")

num2 = input("Ingresar el segundo número: ")
while not num2.isnumeric():
    print("Segundo número ingresado no válido")
    num2 = input("Ingresar el segundo número: ")

num1 = int(num1)
num2 = int(num2)

operacion = input("Ingrese una operación (suma/resta/multiplicacion/division)")
while not(operacion == "suma" or operacion == "resta" or operacion == "multiplicacion" or operacion == "division"):
    print("La operación ingresada no es válida.")
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