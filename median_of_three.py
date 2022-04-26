def median_of_three(nums):
    '''This function returns the number from a list that is of middle value'''
    high = max(nums)
    low = min(nums)
    mids = []
    for num in nums:
        if num == high or num == low:
            del num
        else:
            mids.append(num)
    return mids

print(median_of_three([1, 2, 3]))
print(median_of_three([7, 8, 3]))