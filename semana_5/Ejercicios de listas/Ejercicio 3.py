#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

lista = [10,20,30,40,50,60,70]
memory = lista[len(lista)-1]

for index in range(0,len(lista)):
    if index == 0:
        lista[len(lista)-1] = lista[0]
        lista[0] = memory
    print(lista[index])