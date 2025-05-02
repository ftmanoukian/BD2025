dato = input("Ingrese un número entero: ")

if dato.isnumeric():
    numero = int(dato)
    print("Número ingresado: " + str(numero))
else:
    print("El dato ingresado no representa un número entero")

print("El programa finalizó")