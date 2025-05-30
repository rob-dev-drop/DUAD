#Programa que pide al usuario 3 numeros y busca que la suma de todos sea 30 o bien al menos 1 de los numeros sea 30

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

if (num1 + num2 + num3 == 30 or num1 == 30 or num2 == 30 or num3 == 30):
    print('Correcto')
else:
    print('Incorrecto')