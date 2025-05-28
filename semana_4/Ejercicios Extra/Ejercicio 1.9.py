#El usuario introduce 5 numeros y el programa muestra el mas grande
#Soy conciente de que hay una manera mas efectiva de hacerlo, pero a la hora de hacer el diagrama no sabia jaja

num1 = int(input('Introdunca el primer numero: '))
num2 = int(input('Introdunca el segundo numero: '))
num3 = int(input('Introdunca el tercer numero: '))
num4 = int(input('Introdunca el cuarto numero: '))
num5 = int(input('Introdunca el quinto numero: '))

if (num1 > num2):
    if (num1 > num3):
        if (num1 > num4):
            if (num1 > num5):
                print(f'El numero {num1} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
        else:
            if (num4 > num5):
                print(f'El numero {num4} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
    else:
        if (num3 > num4):
            if (num3 > num5):
                print(f'El numero {num3} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
        else:
            if (num4 > num5):
                print(f'El numero {num4} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
else:
    if (num2 > num3):
        if (num2 > num4):
            if (num2 > num5):
                print(f'El numero {num2} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
        else:
            if (num4 > num5):
                print(f'El numero {num4} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
    else:
        if (num3 > num4):
            if (num3 > num5):
                print(f'El numero {num3} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
        else:
            if (num4 > num5):
                print(f'El numero {num4} es el mas grande')
            else:
                print(f'El numero {num5} es el mas grande')
