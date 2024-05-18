edad = input("Por favor, ingrese la edad del cliente: ")


if edad.isdigit():
    edad = int(edad)
    if edad < 0:
        print("La edad no puede ser negativa. Por favor, ingrese una edad válida.")
    elif edad < 4:
        print("El precio de la entrada es 0€.")
    elif 4 <= edad <= 18:
        print("El precio de la entrada es 5€.")
    else:
        print("El precio de la entrada es 10€.")
else:
    print("Por favor, ingrese un número válido para la edad.")
