lista_feria = ['cebollino', 'chile', 'papas', 'camote']
lista_cuanto = [1,7,14,20]

compras = {}

for index in range(0,len(lista_feria)):
    compras[lista_feria[index]] = lista_cuanto[index]

print(compras)