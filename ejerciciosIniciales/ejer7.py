# Acepte tres cadenas cualquiera de una llamada input(). 
# Escriba un programa para tomar tres nombres como entrada de un usuario 
# con una única llamada a función input().

usuarios = input('Escriba tres nombres: ')
nombres = usuarios.split(' ');

print(f'El primer nombre es {nombres[0]}, el segundo es {nombres[1]} y el tercero es {nombres[2]}')


