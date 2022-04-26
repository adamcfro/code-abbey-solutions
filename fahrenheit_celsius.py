def fahr_to_cels(num):
    '''This funciton converts fahrenheit to celsius'''
    celsius = (num - 32) * (5 / 9)
    return celsius

print(fahr_to_cels(212))