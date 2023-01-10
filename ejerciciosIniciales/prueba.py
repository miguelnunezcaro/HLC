print('Hola Mundo')

nombre = input('Introduzca su nombre por pantalla: ')
edad = input('Introduzca su edad por pantalla: ')

# Primer comentario

print(f'Hola {nombre}, tienes {edad} años')

frase = 'Hola'

print(len(frase))

lista = ['Mandarina', 'Naranja', 'Manzana', 'Fresa']
diccionario = {'uno':1, 'dos':2, 'tres':3}

print('hola', end=' ')
print('adios')
print(lista)
print(diccionario)
num = 5;
print(type(num))

if num == 5:
    print('El número es 5')
else: 
    print('El número no es 5')

fruta = input('Escribe tu fruta para ver si esta en la lista: ')

if fruta in lista:
    print('Tu fruta esta en la lista')
else: 
    print('Tu fruta no esta en la lista')
