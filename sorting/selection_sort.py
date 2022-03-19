# ----------
# Selection sort appends the smallest item of the unsorted sublist to the end of sorted sublist.
# https://en.wikipedia.org/wiki/Selection_sort
# ----------

import random

def selection_sort(unsorted_list):
    unsorted = unsorted_list.copy()
    sorted = []
    while len(unsorted) > 0:
        smallest = unsorted[0]
        index = 0
        for i in range(len(unsorted)):
            if unsorted[i] < smallest:
                smallest = unsorted[i]
                index = i
        sorted.append(unsorted.pop(index))
    return sorted

if __name__ == "__main__":
    unsorted_list = [random.randint(0, 20) for i in range(10)]  
    sorted_list = selection_sort(unsorted_list)
    print(unsorted_list)
    print(sorted_list)