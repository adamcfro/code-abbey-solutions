def rotate_string(num, text):
    '''This function accepts a string and a starting index position, and returns the string with everything in the string up to the index number and moves it to the end of the string.'''
    new_string = text[num:] + text[:num]
    return new_string

print(rotate_string(3, 'forwhomthebelltolls'))
print(rotate_string(-6, 'verycomplexnumber'))