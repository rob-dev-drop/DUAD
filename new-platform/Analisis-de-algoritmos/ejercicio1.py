# Ejercicio de Análisis de Algoritmos #1

def bubble_sort(arr): 
    n = len(arr)                                        # O(1)                             
    for i in range(n-1):                                # O(n)                             
        for j in range(n-1-i):                          # O(n^2)                  
            if arr[j] > arr[j + 1]:                     # O(1)                
                arr[j], arr[j +1] = arr[j+1], arr[j]    # O(1) 
                print("Swaping")                        # O(1)   


my_list = [24, -16, 88, 4, -7, 21, -26]                 # O(1)      

print(my_list)                                          # O(1) 

bubble_sort(my_list)                                    # O(1) 

print(my_list)                                          # O(1)