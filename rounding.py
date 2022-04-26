from decimal import Decimal, ROUND_HALF_UP

def rounding(*args):
    '''This function divides the first argument passed by the second argument passed and rounds to the nearest integer'''
    my_list = []
    for nums in args:
        a, b = nums
        new_num = int(round((a / b) + 0.00001)) # rounding is not always accurate so I added to make sure that anything at .5 rounded up

        my_list.append(new_num)
    return my_list



print(rounding([10, 5], [7, 4], [5, 2], [5, 4]))