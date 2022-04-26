def bubble_in_array(lst):
    '''This function takes in a list and swaps integers if the current integer is greater than the next integer.'''
    counter = 0
    swaps = 0
    for num in range(len(lst) - 1):
        counter += 1
        if num == -1 or lst[num + 1] == -1:
            continue
        else:
            if lst[num] > lst[num + 1]:
                lst[num], lst[num + 1] = lst[num + 1], lst[num]
                swaps += 1
                bubble_in_array(lst[num:])
            else:
                continue
    return swaps, lst
        


print(bubble_in_array([1, 4, 3, 2, 6, 5, -1]))

# note: only sorts once

