from random import uniform
from math import ceil

def dice_rolling(*args):
    '''This function generates random values between 0 and 1, multiplies them by 6 and rounds them.'''
    rand_num = uniform(0, 1) * 6
    dice_roll = ceil(rand_num)
    return f"Given number: {rand_num}. Dice roll: {dice_roll}."

print(dice_rolling())
