#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41

lista_gbl = []

def sumar_elementos_lista(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma


total_elementos = int(input('Ingrese la cantidad de elementos de desea sumar: '))
counter = 0

while total_elementos > counter:
    num = int(input(f'Ingrese el numero (quedan {total_elementos - counter})'))
    lista_gbl.append(num)
    counter += 1

result = sumar_elementos_lista(lista_gbl)
print(f'La suma de los elementos de la lista es de: {result}')