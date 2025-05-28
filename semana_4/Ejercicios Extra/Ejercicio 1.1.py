precio_producto = int(input("Ingrese el precio del producto: "))
descuento = 0
precio_final = 0
if (precio_producto >= 100):
    descuento = precio_producto*0.10
else:
    descuento = precio_producto*0.02
precio_final = precio_producto-descuento
print(f'El precio con descuento es de {int(precio_final)}') #Investigando aprendi que como estoy dividiendo por un float, el resultado resulta en un float, por eso lo pido como un int a la hora de mostrarlo al final