def bubble_sort(arr): 
    n = len(arr)                                          
    for i in range(n-1):   
        print(f"======== Iteracion {i+1} ========")                             
        for j in range(n-1,i,-1):                                                   #Added a range with -1 step so it goes backwards, stops as i so each iteration dont check on those that are already arranged
            print(f"Elemento {j+1} es {arr[j]} y se compara con {arr[j-1]}")
            if arr[j] < arr[j-1]:                                                  
                arr[j], arr[j-1] = arr[j-1], arr[j]
            print(my_list)
        print("")

my_list = [24, -16, 88, 4, -7, 21, -26]      
print(my_list)
bubble_sort(my_list)
#print(my_list)


