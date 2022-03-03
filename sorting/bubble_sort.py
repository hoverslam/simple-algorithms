def bubble_sort(unsorted_list):
    my_list = unsorted_list.copy()   
    while True:
        swapped = False
        for i in range(1, len(my_list)):
            if my_list[i-1] > my_list[i]:
                my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
                swapped = True
                
        if not swapped:
            return my_list
    
unsorted_list = [5, 3, 9, 2, 5, 1, 4, 2, 8]   
sorted_list = bubble_sort(unsorted_list)
print(unsorted_list)
print(sorted_list)