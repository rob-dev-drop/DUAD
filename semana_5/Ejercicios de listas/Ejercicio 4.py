#Cree un programa que elimine todos los números impares de una lista.

lista = [45,56,76,33,50,11]

for index, listn in enumerate(lista):
    if listn%2 != 0:
        lista.pop(index)

print(lista)
