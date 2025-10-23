from datetime import date

def check_age(func): #decorator that checks user age and determines if user is adult or raises an error if user is underage
    def wrapper(self):
        userage = func(self)
        if userage < 18:
            raise ValueError
        else:
            print('User is adult')
        return userage
    return wrapper

class User:
    def __init__(self, mm, dd, yy):
        self.date_of_birth = {
            'month': mm,
            'day': dd,
            'year': yy
        }
    @property #The order here will allow the age property to always check the user age
    @check_age
    def age(self):
        today = date.today()
        userage = today.year - self.date_of_birth['year'] - ((today.month,today.day) <(self.date_of_birth['month'],self.date_of_birth['day']))
        return userage


user_1 = User(11,30,1997)
print(f'User is: {user_1.age} years old')


