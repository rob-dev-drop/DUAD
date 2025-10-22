#Cree un decorador que haga print de los parámetros y retorno de la función que decore.


#def decorator_name(func):
#    def wrapper(parameters):
#        #logica extra
#        func(parameters)
#        #logica extra
#        
#    return wrapper

def numcheck(func):
    def wrapper(number1,number2):
        print(f'Numbers entered are {number1} & {number2}')
        print(f'Result is: {func(number1,number2)}')
    return wrapper


@numcheck
def numsum(number1,number2):
    result = number1 + number2
    return result

numsum(2,8)