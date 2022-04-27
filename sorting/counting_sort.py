# ----------
# Counting Sort has an O(n) runtime, but only works for integers
# https://en.wikipedia.org/wiki/Counting_sort
# ----------

import random

def counting_sort(unsorted_list):
    min_int = min(unsorted_list)
    max_int = max(unsorted_list)
    counts = [0] * (max_int - min_int + 1)
    sorted_list = [None] * (len(unsorted_list))
    
    for value in unsorted_list:
        counts[value - min_int] += 1
        
    for i in range(len(counts)-1):
        counts[i+1] += counts[i] 
    
    for value in unsorted_list:
        index = value - min_int
        sorted_list[counts[index]-1] = value
        counts[index] -= 1
        
    return sorted_list

if __name__ == "__main__":
    unsorted_list = [random.randint(-1000, 1000) for i in range(10)]  
    sorted_list = counting_sort(unsorted_list)
    print(unsorted_list)
    print(sorted_list)