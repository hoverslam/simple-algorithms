# ----------
# Bubble sort compares adjacent elements and swaps them if they are in the wrong order.
# https://en.wikipedia.org/wiki/Bubble_sort
# ----------

import random

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


if __name__ == "__main__":
    unsorted_list = [random.randint(0, 20) for i in range(10)]  
    sorted_list = bubble_sort(unsorted_list)
    print(unsorted_list)
    print(sorted_list)