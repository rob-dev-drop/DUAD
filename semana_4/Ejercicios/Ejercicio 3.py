#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

num_secreto = random.randint(1,10)
resolved = False
while (not resolved):
    num = int(input('Adivina el numero secreto del 1 al 10: '))
    if (num != num_secreto):
        print('Intenta de nuevo')
    else:
        print(f'Acertaste, el numero secreto es {num_secreto}')
        resolved = True

