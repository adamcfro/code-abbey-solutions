def min_of_three(*args):
    '''This program takes in lists of three numbers and returns the lowest number.'''
    my_list = []
    for nums in args:
        smallest = min(nums)
        my_list.append(smallest)
    return my_list


print(min_of_three([7, 3, 5], [15, 20, 40], [300, 550, 137]))