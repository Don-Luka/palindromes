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

# alternatywna wersja funkcji palindromy

def palindrome_alt(word, case_sensitive = False):
    '''
    This function checks wether given word is a palindrome, 
    i.e. if there's no matter if it's read forwards or backwards, 
    e.g. "kajak", using whole lists comparison.
    The case_sensitive parameter tells if we care about upper- or lowercase.
    '''
    if case_sensitive == False:
        word = word.casefold()
    letters = [letter for letter in word]
    letters_reversed = letters.copy()
    letters_reversed.reverse()

    return letters_reversed == letters

print(palindrome_alt('Maoam', case_sensitive=False))
