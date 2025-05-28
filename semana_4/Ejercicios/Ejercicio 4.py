#Cree un programa que le pida tres números al usuario y muestre el mayor.

contador = 3
memory = 0
while (contador > 0):
    num = int(input(f'Ingresa un numero (faltan {contador})'))
    if (num > memory):
        memory = num
        contador -= 1
    else:
        contador -= 1

print (f'El numero mas grande es {memory}')