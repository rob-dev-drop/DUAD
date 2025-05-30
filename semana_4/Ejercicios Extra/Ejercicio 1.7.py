#Usuario debe adivinar numero secreto y el programa no acaba hasta que lo logra

num_secreto = 9
solved = False

while (solved == False):
    num = int(input('Adivina el numero secreto del 1 al 10: '))
    if (num != num_secreto):
        print('intenta de nuevo')
    else:
        print('Adivinaste!')
        solved = True 