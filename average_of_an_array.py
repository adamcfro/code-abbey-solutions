def average_of_array(lst):
    '''This function takes in a list of numbers, sums them together and divides by the length of the list (without taking in the zero for sum or length).'''
    total = 0
    for num in lst:
        total += num
    new_total = round(total / (len(lst) - 1))
    return new_total


print(average_of_array([1, 2, 3, 0]))
print(average_of_array([7, 14, 2, 0]))
print(average_of_array([8, 8, 7, 2, 0]))


