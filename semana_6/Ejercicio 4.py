#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

def request_name():
    name = input("Ingrese su nombre y apellido: ")
    return name


def set_backwards():
    name = request_name() #Las variables de 'name' dentro de las funciones tienen el mismo nombre, pero como son locales para cada funcion no interfieren con su funcionamiento en cada funcion
    display_name = ""
    for char in range(len(name)-1,-1,-1):
        display_name = display_name + name[char]
    return display_name

print(set_backwards())