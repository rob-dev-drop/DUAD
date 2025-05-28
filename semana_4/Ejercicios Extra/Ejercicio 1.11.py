#El pide 100 numeros al usuario y muestra la suma de todos

finished = False
contador = 100
suma = 0

while (not finished):
    if (contador != 0):
        num = int(input(f'Ingrese un numero (faltan {contador})'))
        suma = suma + num
        contador -= 1
    else:
        finished = True

print(f"La suma de los numeros es {suma}")