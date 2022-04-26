def arith_prog(start, step, to_count):
    '''This function takes a start, a step, and a number of times to increment, then sums the numbers in the list'''
    my_list = [start]
    next_step = start
    for item in range(1, to_count):
        next_step += step
        my_list.append(next_step)
    total = 0
    for item in my_list:
        total += item
    return total


print(arith_prog(5, 2, 3))
print(arith_prog(3, 0, 10))
print(arith_prog(2, 3, 5))