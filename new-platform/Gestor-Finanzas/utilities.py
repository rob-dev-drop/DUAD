

def number_validation(num):
        try: 
            x = float(num)
            if x > 0:
                return True
            elif x <= 0:
                raise ValueError
        except ValueError:
            return False
        

