def sum_in_loop(*args):
    '''This function takes in any amount of numbers and sums them together.'''
    total = 0
    for num in args:
        total += num
    return total

print(sum_in_loop(1, 2, 3, 4))