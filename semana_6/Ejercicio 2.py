#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.

global_var = 333


def multiplicar_numero():
    decada = 10
    cantidad_de_decadas = decada * global_var
    result = cantidad_de_decadas
    return result

print(multiplicar_numero()) # La funcion me deja accesar la variuable global y utilizarla dentro de la funcion

print(decada) # No me deja acceder al valor de esta variable porque es local en multiuplicar_numero()


