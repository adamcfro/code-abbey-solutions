def triangles(a, b, c):
    '''This program takes in three side lengths and determines if they could make a triangle.'''
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        return True
    else:
        return False

print(triangles(1, 2, 3))
print(triangles(6, 2, 3))
print(triangles(1, 2, 4))