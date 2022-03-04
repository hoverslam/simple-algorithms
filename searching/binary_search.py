# ----------
# Binary search finds the position of a target value within a sorted list by looking at the middle element and eliminate the half in which the target cannot lie.
# https://en.wikipedia.org/wiki/Binary_search_algorithm
# ----------

import math, random

def linear_search(seq, target):
    low = 0
    high = len(seq) - 1
    
    while low <= high:
        i = math.floor((low + high) / 2)
        if seq[i] < target:
            low = i + 1
        elif seq[i] > target:
            high = i - 1
        else:
            return i            
        
    return -1    # -1 when element not found


if __name__ == "__main__":
    my_list = [random.randint(0, 40) for i in range(20)]
    target = 10
    index = linear_search(my_list, target)
    if index != -1:
        print("{} first found at index {} in {}.".format(target, index, my_list))
    else: 
        print("{} not found in {}.".format(target, my_list))