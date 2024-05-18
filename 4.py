# Grupo 3
# Ejercicio 4.
# Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla la cuenta atrás desde ese número hasta cero.
número1 = int(input("Ingresa un número entero positivo: "))

if número1 <= 0 :
     print("ERROR")

else:
    for i in range(número1,0-1,-1):
     print(i)
