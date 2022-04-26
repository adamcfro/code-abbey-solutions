def gcd(a, b):
    '''This function takes in two numbers, then finds the greatest common denominator between them and the least common multiple.'''
    new_list = []
    for num in range(1, b):
        if a % num == 0 and b % num == 0:
            new_list.append(num)
        else:
            if 1 not in new_list:
                new_list.append(1)
    gcd = max(new_list)
    lcm = int((a * b) / gcd)

    return gcd, lcm


print(gcd(2, 3))
print(gcd(4, 10))