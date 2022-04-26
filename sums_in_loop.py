def sums_in_loop(*args):
    '''This function takes in pairs of numbers and returns their sums.'''
    sums = []
    for item in args:
        total = sum(item)
        sums.append(total)
    return sums

print(sums_in_loop([1, 2], [3, 4], [5, 6]))