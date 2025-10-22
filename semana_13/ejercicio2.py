#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def numbercheck(func):
    def wrapper(num1,num2):
        try:
            if isinstance(num1, int) == False or isinstance(num2, int) == False:
                raise ValueError()
            else:
                print(func(num1,num2))
        except ValueError:
            print('One or both arguments are not numbers')
    return wrapper

@numbercheck
def suma(num1,num2):
    x = num1 + num2
    return x

#Decorator checks that both arguments are numbers and gives the result, result is printed from the decorator, not the fuction alone
suma(5, 4)

#decorator checks that the letter "f" is not a number and raises a ValueError and shows the corresponding message
suma("f", 4)

