#El programa le pide al usuario 100 numeros y le muestra el mayor

contador = 100
memoria = 0
finished = False

while (not finished):
    if (contador != 0):
        num = int(input(f'Ingrese el numero (faltan {contador}): '))
        if (memoria < num):
            memoria = num
            contador -= 1
        else:
            contador -= 1
    else:
        print(f'El numero mas grande es {memoria}')
        finished = True

