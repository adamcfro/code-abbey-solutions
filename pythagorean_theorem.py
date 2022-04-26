def p_theorem(a, b, c):
    '''This function takes in three numbers corresponding to the sides of a triangle and determines if the triangle is right, acute, or obtuse.'''
    if a**2 + b**2 == c**2:
        return "Right"
    elif c**2 < a**2 + b**2:
        return "Acute"
    elif c**2 > a**2 + b**2:
        return "Obtuse"
    else:
        return "Not a triangle"


print(p_theorem(6, 8, 9))
print(p_theorem(9, 12, 15))
print(p_theorem(16, 12, 22))
