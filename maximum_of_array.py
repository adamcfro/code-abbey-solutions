def max_of_array(*args):
    '''This program takes in a list of numbers and returns the lowest and highest numbers.'''
    for num in args:
        max_num = max(num)
        min_num = min(num)
    return min_num, max_num


print(max_of_array([3, 1, 324, 34, 2452, 35, 23, 345, 33]))