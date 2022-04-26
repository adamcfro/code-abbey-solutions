def array_counters(array):
    return [[x, array.count(x)] for x in set(array)]

mylist = [3, 2, 1, 2, 3, 1, 1, 1, 1, 3]
print(array_counters(mylist))


########


from collections import Counter

def array_counters(array):
    return Counter(array)

mylist = [3, 2, 1, 2, 3, 1, 1, 1, 1, 3]
print(array_counters(mylist))