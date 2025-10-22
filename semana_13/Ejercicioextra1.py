

def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper

@repeat_twice
def printname(name):
    print(f'Hola, {name}')
    

printname('Roberto')