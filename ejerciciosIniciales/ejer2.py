# Escriba un programa para usar el método string.format() para formatear las siguientes tres variables 
# según la salida esperada.

totalMoney = 1000
quantity = 3
price = 450

mensaje = 'Tengo {1} euros para comprar {0} tarjetas gráficas por {2:.2f} dólares.'
print(mensaje.format(quantity,totalMoney,price))