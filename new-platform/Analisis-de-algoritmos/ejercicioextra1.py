# Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

# V1
def manual_add(n): 
    result = 0 #O(1)
    for i in range(1, number + 1): #O(n)
        result += i      #O(1)
    return result        #O(1)

# V2
def add_formula(n):
    return number * (number + 1) // 2      #O(1)


# Preguntas:

#     ¿Cuál es la complejidad de cada versión?
#      V1: O(n)
#      V2: O(1)




#     ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
#      Usaria la V2,  porque es solo una linea de codigo que se ejecuta sin que escale la cantidad 
#            de cosas por hacer como lo haria con un ciclo que dependa de la cantidad de elementos n.