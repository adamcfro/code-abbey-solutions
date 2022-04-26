def vowel_count(text):
    '''This function returns the amount of vowels in a given string'''
    count = 0
    for letter in text:
        if letter in 'aeiouy':
            count += 1
    return count

print(vowel_count("Hi, how are you doing today?"))