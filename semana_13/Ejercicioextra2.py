
user_logged_in = True

def requires_login(func):
    def wrapper(*args):
        try:
            if user_logged_in == True:
                print('User is logged in')
                func()
            else:
                raise ValueError
        except ValueError:
            print("User is not authenticated")
    return wrapper

@requires_login
def view_sensitive_data():
    print("Here is the sensitive data")


view_sensitive_data()