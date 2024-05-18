'''7. Escribir un programa que muestre por pantalla la tabla de multiplicar del
1 al 10.'''
for i in range(1,11):
    print(f'\nTabla de multiplicar del {i}')
    for j in range(1,13):
        resultado = i *j
        print(f'{j} * {i} = {resultado}')
