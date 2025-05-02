num1 = input("Ingrese el primer número (natural): ")
num2 = input("Ingrese el segundo número (natural): ")
operacion = input("Ingrese la operación (suma/resta/multiplicacion/division): ")

num1 = int(num1)
num2 = int(num2)

if operacion == "suma" or operacion == "+":
    resultado = num1 + num2
    resultado = str(resultado)
    print("El resultado es " + resultado)
elif operacion == "resta" or operacion == "-":
    resultado = num1 - num2
    resultado = str(resultado)
    print("El resultado es " + resultado)
elif operacion == "multiplicacion" or operacion == "*" or operacion == "x":
    resultado = num1 * num2
    resultado = str(resultado)
    print("El resultado es " + resultado)
elif operacion == "division" or operacion == "/" or operacion == ":":
    resultado = num1 / num2
    resultado = str(resultado)
    print("El resultado es " + resultado)
else:
    print("Operación no válida")