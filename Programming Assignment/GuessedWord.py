def getGuessedWord(secretWord,lettersGuessed):
    if(lettersGuessed[1] == ' ' and lettersGuessed[2] == ' ' and lettersGuessed[3] == ' '):
        global returnstringT
        returnstring = ['* ','* ','* ','* ','* ','* ','* ']
        returnstringT = [ ]
    else:
        returnstring = returnstringT
        
    if(lettersGuessed[0] == 'm'):
            returnstring[0] = 'm'
    else:
           pass
    if(lettersGuessed[1] == 'o'):
            returnstring[1] = 'o'
    else:
           pass
    if(lettersGuessed[2] == 'n'):
            returnstring[2] = 'n'
    else:
           pass
    if(lettersGuessed[3] == 's'):
            returnstring[3] = 's'
    else:
           pass
    if(lettersGuessed[4] == 't'):
            returnstring[4] = 't'
    else:
           pass 
    if(lettersGuessed[5] == 'e'):
            returnstring[5] = 'e'
    else:
           pass 
    if(lettersGuessed[6] == 'r'):
            returnstring[6] = 'r'
    else:
        pass 
    
    returnstringT = returnstring
    print (''.join(returnstring))
    return returnstring     