# ----------
# Insertion sort iterates removes one element from the unsorted list, finds the location it belongs within the sorted list, and inserts it there.
# https://en.wikipedia.org/wiki/Insertion_sort
# ----------

import random

def insertion_sort(unsorted_list):
    my_list = unsorted_list.copy()
    for i, value in enumerate(my_list):
        j = i - 1
        while j >= 0 and my_list[j] > value:
           my_list[j+1] = my_list[j]
           j = j - 1
        my_list[j+1] = value
    return my_list         

if __name__ == "__main__":
    unsorted_list = [random.randint(0, 20) for i in range(10)]  
    sorted_list = insertion_sort(unsorted_list)
    print(unsorted_list)
    print(sorted_list)