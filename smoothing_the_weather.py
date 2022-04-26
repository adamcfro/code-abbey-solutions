def smoothing(lst):
    '''This function takes in a list of numbers and returns a list of numbers where the current number, the previous number, and the following number are added together then divided by three. The first and last numbers are untouched.'''
    my_list = []
    my_list.append(lst[0])
    for i in range(1, len(lst) - 1):
        number = (lst[i] + lst[i + 1] + lst[i - 1]) / 3
        # number = sum(lst[i - 1: i + 2]) / 3
        my_list.append(number)
    my_list.append(lst[-1])
    return my_list


print(smoothing([32.6, 31.2, 35.2, 37.4, 44.9, 42.1, 44.1]))


try this with enumerate