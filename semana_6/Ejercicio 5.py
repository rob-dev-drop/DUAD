#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def request_text():
    text = input('Ingrese el texto: ')
    return text

def count_cases():
    mayus = 0
    minus = 0
    for char in request_text():
        if char.isupper() == True:
            mayus += 1
        elif char == " ":
            minus + 0 
        else:
            minus += 1
    print(f'Hay {mayus} letras mayusculas y {minus} minusculas')

count_cases()