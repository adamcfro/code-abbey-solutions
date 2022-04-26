def bike_race(dist, a, b):
    '''This function takes in a distance in kilometers, and the speed of two bicyclists in kilometers per hour. It calculates the point at which the two bicyclists will meet based on their speed and the distance between them.'''
    spot = dist/(a + b)
    return spot

print(bike_race(10, 1, 1))
print(bike_race(20, 1, 2))