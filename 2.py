'''2. Escribir un programa que pregunte al usuario una cantidad a invertir, el
interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.'''

cant = float(input('Ingrese la cantidad a invertir (S/)?: '))
capital = cant
interes = float(input('Ingrese el interes (%): '))
years = int(input('Ingrese los años de inversion: '))
for i in range(1,years+1):
    capital += cant * (interes/100)
    print(capital)
