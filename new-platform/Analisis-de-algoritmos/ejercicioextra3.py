

# Analice la siguiente función:


def print_all_pairs(my_dict):
    for key1 in my_dict:               #O(n)
        for key2 in my_dict:           #O(n^2)
            print(f"{key1}-{key2}")    #O(1)


# Preguntas:

#     ¿Cuál es la complejidad temporal?
#      La complejidad es #O(n^2)
#     ¿Cuanto dura si hay 1 millón de claves?
#       Dura O(1000000^2), el tiempo en segundos depende del hardware donde se ejecute y el contenido del diccionario