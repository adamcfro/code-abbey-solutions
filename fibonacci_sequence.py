def fibonacci_seq(num):
    '''This program takes in a number and finds the index at which the number is found in the fibonacci sequence.'''
    a = 0
    b = 1
    fib_list = [a]
    while num not in fib_list:
        a, b = b, a + b
        fib_list.append(a)
    return f"Fibonacci number {num} found at index {len(fib_list) -1}"

print(fibonacci_seq(610))
print(fibonacci_seq(34))
print(fibonacci_seq(0))