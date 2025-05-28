num = int(input('Introduzca un numero para mostar la suma de todos los numeros de 1 hasta el: '))
counter = num
suma = 0
while(counter != 0):
    suma = suma + counter
    counter -= 1
print(f'La suma de los numeros de uno hasta {num} es de {suma}') 