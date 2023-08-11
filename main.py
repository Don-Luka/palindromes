# Funkcja palindromy

def palindrome(word):
    '''
    This function checks wether given word is a palindrome, 
    i.e. if there's no matter if it's read forwards or backwards, 
    e.g. "kajak", using one-by-one character comparison.
    '''
    is_palindrome = True
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            is_palindrome = False
        else:
            pass
    return is_palindrome


print(palindrome('maoam'))