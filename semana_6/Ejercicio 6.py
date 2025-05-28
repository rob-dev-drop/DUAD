#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

unsortedtxt = "python-variable-funcion-computadora-monitor"

def create_word_list():
    lista_palabras = []
    temp_char = ""
    while True:
        for char in unsortedtxt:
            if char != "-":
                temp_char = temp_char + char
            else:
                lista_palabras.append(temp_char)
                temp_char = ""
        break
    lista_palabras.append(temp_char)
    return lista_palabras


def print_sorted():
    lista = create_word_list()
    counter = 0
    final_string = ""
    for word in sorted(lista):
        if counter < len(lista)-1:
            final_string = final_string + word + "-"
        else:
            final_string = final_string + word
        counter += 1
    return final_string

print(print_sorted())
