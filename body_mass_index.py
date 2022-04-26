def convert_weight(pounds):
    '''Converts pounds to kilograms.'''
    return round(pounds * 0.453592, 4)

def convert_height(inches):
    '''Converts inches to centimeters.'''
    return round(inches * 0.0254, 4)


print(convert_weight(190))
print(convert_height(71))


def body_mass_index(weight, height):
    '''This function takes a weight in kilograms and a height in centimeters and provides a BMI for that person'''
    return round(weight / (height ** 2), 3)
print(body_mass_index(convert_weight(190), convert_height(71)))