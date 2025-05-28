# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

lista_numeros = [10,22,37,45,56]
lista_letras = ["Fresas","Uvas","Arandanos","Mangos","Pitayas"]

times = len(lista_numeros)
count = 0
stage = 0
print("Lista del mercado:")
while (times > count):

    for index in range(0,len(lista_numeros)):
        impresion = lista_numeros[index + stage]
        break
    for index2 in range(0,len(lista_letras)):
        impresion2 = lista_letras[index2+ stage]
        break
    print(f'{impresion} {impresion2}')
    count +=1
    stage +=1                    