# Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:            #O(n)
        if item == target:          #O(1)
            return True             #O(1)
    return False                    #O(1)


def binary_search(my_list, target):
    low = 0                            #O(1)
    high = len(my_list) - 1            #O(1)
    while low <= high:                 #O(LogN)
        mid = (low + high) // 2        #O(1)
        if my_list[mid] == target:     #O(1)
            return True                #O(1)
        elif my_list[mid] < target:    #O(1)
            low = mid + 1              #O(1)
        else:                          
            high = mid - 1             #O(1)
    return False                       #O(1)



# Preguntas:

#     ¿Cuál es la complejidad de cada algoritmo?
#     El primero tiene una complejidad de O(n) mientras que el segundo es OLog(n)

#     ¿En qué condiciones conviene usar cada uno?
#      El segundo reduce la cantidad de iteraciones considerablemente, por lo que en busquedas grandes es muy eficiente, pero depende de que la lista este ordenada. 
#      El primero reocorre toda la lista, en mas pasos, pero no depende de que la lista este ordenada.


#     ¿Qué pasa si la lista no está ordenada?
#     El binary search daria un resultado incorrecto/ return False. El linear search busca en todos los indices de la lista para ver si hace match
#     con el target, entonces funciona aunque la lista este desordenada.