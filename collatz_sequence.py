def collatz_sequence(num):
    '''This function takes in a number. If the number is odd, the number grows. If it is even, the number decreases. This function calculates how many sequences it takes to reach 1.'''
    sequence = [num]
    counter = 0
    while num != 1:
        counter += 1
        if num % 2 == 0:
            num = int(num / 2) # do i need int here?
            sequence.append(num)
        else:
            num = num * 3 + 1
            sequence.append(num)
    return counter


counter = 0


print(collatz_sequence(2))
print(collatz_sequence(15))
print(collatz_sequence(97))
