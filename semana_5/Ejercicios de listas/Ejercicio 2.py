#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
elestrin = "Roberto"
for index in range(len(elestrin)-1, -1, -1):
    print(f'{elestrin[index]}')