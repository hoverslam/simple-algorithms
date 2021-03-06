# ----------
# Binary search finds the position of a target value within a sorted list by looking at the middle element and eliminate the half in which the target cannot lie.
# https://en.wikipedia.org/wiki/Binary_search_algorithm
# ----------

import math, random

def linear_search(seq, target):
    low = 0
    high = len(seq) - 1
    
    while low <= high:
        mid = math.floor(low + (high - low) / 2)
        if seq[mid] < target:
            low = mid + 1
        elif seq[mid] > target:
            high = mid - 1
        else:
            return mid            
        
    return -1    # -1 when element not found


if __name__ == "__main__":
    my_list = sorted([random.randint(0, 40) for i in range(20)])
    target = 10
    index = linear_search(my_list, target)
    if index != -1:
        print("{} first found at index {} in {}.".format(target, index, my_list))
    else: 
        print("{} not found in {}.".format(target, my_list))