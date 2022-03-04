# ----------
# Linear search sequentially checks each element of the list until a match is found or the whole list has been searched.
# https://en.wikipedia.org/wiki/Linear_search
# ----------

import random

def linear_search(seq, target):
    index = -1
    for i in range(len(seq)):
        if seq[i] == target:
            index = i
            break
            
    return index    # -1 when element not found


if __name__ == "__main__":
    my_list = [random.randint(0, 40) for i in range(20)]
    target = 10
    index = linear_search(my_list, target)
    if index != -1:
        print("{} first found at position {} in {}.".format(target, index, my_list))
    else: 
        print("{} not found in {}.".format(target, my_list))