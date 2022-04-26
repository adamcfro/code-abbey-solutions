def weighted_sum(num):
    '''This function takes each individual number of a multi-digit number, multiplies them by their position(+1), and then sums those numbers'''
    my_list = []
    counter = 1
    for i in str(num):
        my_list.append(int(i) * counter)
        counter += 1
    return my_list


print(weighted_sum(1776))