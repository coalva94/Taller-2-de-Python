'''6. Los alumnos de un curso se han dividido en dos grupos A y B de
acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres
con un nombre anterior a la M y los hombres con un nombre posterior a
la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le
corresponde.'''
def student(name,sex):
    if name <= 'M' and sex == 'F':
        print('El alumn@ pertence al grupo A')
    elif name >= 'N' and sex =='M':
        print('El alumn@ pertence al grupo A')
    else:
        print('El alumn@ pertence al grupo B')
    return
name = input('Ingrese el nombe del alumn@: ').capitalize()
sex = input('Ingrese el sexo del alumn@ (M/F:) ').upper()
student(name,sex)
