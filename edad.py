#Script : edad

'''
aplicacion ingreso de datos
'''

fecha=2020
nombre=0
nacimiento=0
edad=0
print ('digite su nombre:')

nombre = input()

print ('digite su año de nacimiento:')

nacimiento = int (input())

#PROCESS

edad = fecha - nacimiento

print ('la edad de ',nombre, 'es', edad)
