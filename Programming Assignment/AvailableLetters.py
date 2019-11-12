def getAvailableLetters(lettersGuessed):
    import string
    alphabet=list(string.ascii_lowercase)
    alphabetset=set(alphabet)
    guessedLetters=set(lettersGuessed)
    usableLetters=alphabetset.difference(guessedLetters)
    print(" ".join(sorted(usableLetters, reverse=False)))
    return usableLetters