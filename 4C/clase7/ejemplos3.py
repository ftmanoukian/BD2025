
while True:
    try:
        num_usuario = float(input("Ingrese un número flotante: "))
        break
    except ValueError:
        print("El dato ingresado no es válido. Intente nuevamente.")

print(num_usuario)