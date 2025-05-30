#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

lista = []

counter = 10
memory = 0

while (counter > 0) :
    num = int(input(f"ingrese un numero, faltan {counter}: "))
    lista.append(num)
    if (memory < num):
        memory = num
        counter -=1
    else:
        counter -=1

print (f'{lista} el numero mas alto es: {memory}')
