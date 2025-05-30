#Pide un numero al usuario y verifica si es divisible entre 3 o 5

solved = False
while (not solved):
    num = int(input('Ingrese un numero divisible entre 3 y/o 5: '))
    if (num%5 == 0 and num%3 == 0):
        print("FizzBuzz")
        solved = True
    elif (num%5 == 0 and num%3 !=0):
        print("Buzz")
        solved = True
    elif (num%5 != 0 and num%3 ==0):
        print("Fizz")
        solved = True
    else:
        print("El numero no es divisible entre 3 ni 5")
