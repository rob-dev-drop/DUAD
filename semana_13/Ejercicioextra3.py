from datetime import datetime
from functools import wraps



def validate_numbers(func):
    @wraps(func)
    def wrapper(num1,num2):
        try:
            if isinstance(num1, int) == False or isinstance(num2, int) == False:
                raise ValueError()
            else:
                print('Valid numbers')
        except ValueError:
            print('One or both arguments are not numbers')
        return func(num1,num2)
    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        current_date = datetime.now()
        print(f'Calling {func.__name__} with numbers {args}, on {current_date} and the result is {result}')
        print(f'Result is {result}')
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(num1,num2):
    result = num1 * num2
    return result


multiply(2,4)