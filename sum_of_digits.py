def sum_of_digits(num):
    '''This function returns the sum of each individual number in a multi-digit number'''
    return sum([int(i) for i in str(num)])

print(sum_of_digits(123))
