#Cree un decorador que haga print de los parámetros y retorno de la función que decore.


#def decorator_name(func):
#    def wrapper(parameters):
#        #logica extra
#        func(parameters)
#        #logica extra
#        
#    return wrapper

def numcheck(func):
    def wrapper(*args,**kwargs): #since are used as a list, I iterated it so it would show all arguments entered
        lista = []
        print('Numbers entered:')
        for i,arg in enumerate(args):
            print(f'{args[i]}')
        func(*args)
    return wrapper


@numcheck
def numsum(*args): #changed this to *args so the function can use any amount of numbers
    result = 0
    for i in args:
        result += i
    print(result)
    return result

numsum(2,5,10)