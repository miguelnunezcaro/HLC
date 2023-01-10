# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, 
# devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.

num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce otro número: '))

suma = num1 + num2;
producto = num1 * num2;

if producto > 1000:
    print('El número es mayor que 1000, por tanto nos devuelve el producto')
    print(producto)
else:
    print('El número es menor que 1000, por tanto nos devuelve la suma')
    print(suma)

