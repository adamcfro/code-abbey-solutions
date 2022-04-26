def palindromes(text):
    '''This function takes in a string and returns True if the string is equal to the string reversed.'''
    new_string = ''
    for letter in text:
        if letter in ' !?_-.,':
            continue
        else:
            new_string += letter

    return new_string.lower() == new_string[::-1].lower()

print(palindromes('stats'))
print(palindromes('Some men interpret nine memos'))
print(palindromes('O, a kak Uwakov lil vo kawu kakao!'))