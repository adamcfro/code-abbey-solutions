def josephus(people, skip):
    ls = list(range(1, people + 1))
    skip -= 1
    i = skip
    while len(ls) > 1:
        ls.pop(i)
        i = (i + skip) % len(ls)
    return ls[0]

print(josephus(10, 3))