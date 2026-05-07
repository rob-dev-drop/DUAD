def bubble_sort(arr): 
    n = len(arr)                                          # Asigned the length of the list to a variable for simplicity
    for i in range(n-1):                                  # Outer loop, defines the amount of times the list will be iterated
        for j in range(n-1-i):                            # Inner loop, does the comparisons to 'bubble up' (or to the right in this case) the highest value. We substract i from the range so each iteration runs only on those values that are not sorted.
            if arr[j] > arr[j + 1]:                       # Compares the values
                arr[j], arr[j +1] = arr[j+1], arr[j]      # if the current value is higher than the next value, it interchanges their position in the list. I am using In-Place Mutation so there is no need for other variables.
                print("Swaping")                          # Prints Swapping text when it swaps the values


my_list = [24, -16, 88, 4, -7, 21, -26]                   

print(my_list)

bubble_sort(my_list)

print(my_list)

