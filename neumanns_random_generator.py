def neumanns_gen(num):
    '''This function takes in a number, multiplies it by itself, and then removes the two outside digits on both sides. It also counts the number of sequences taken until it repeats one of the created 4-digit numbers.'''
    my_string = [num]
    new_num = 0
    count = 0
    print(num)
    while my_string.count(new_num) < 2:
        num_two = num * num
        new_num = int((num_two / 100) % 10000)
        print(f"{new_num} (8-digit number: {num_two})")
        my_string.append(new_num)
        num = new_num
        count += 1
    return f"{count} sequences taken."


print(neumanns_gen(4100))
print(neumanns_gen(5761))

# Notes: program doesn't work when zero is the first number
# print(neumanns_gen(0001))