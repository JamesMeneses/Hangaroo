def hangaroo(secretWord):
    from WordGuessed import isWordGuessed
    from GuessedWord import getGuessedWord
    from AvailableLetters import getAvailableLetters
    lettersGuessed=[" "," "," "," "," "," "," "]
    print("Welcome to Hangaroo\n")
    
    def Answer(user):
        if(user=='m'):
            lettersGuessed[6]=lettersGuessed[0]
            lettersGuessed[0]='m'
            print("That's the right letter!\n")
            pass
        elif(user=='o'):
            lettersGuessed[6]=lettersGuessed[1]
            lettersGuessed[1]='o'
            print("That's the right letter!\n")
            pass
        elif(user=='n'):
            lettersGuessed[6]=lettersGuessed[2]
            lettersGuessed[2]='n'
            print("That's the right letter!\n")
            pass
        elif(user=='s'):
            lettersGuessed[6]=lettersGuessed[3]
            lettersGuessed[3]='s'
            print("That's the right letter!\n")
            pass
        elif(user=='t'):
            lettersGuessed[6]=lettersGuessed[4]
            lettersGuessed[4]='t'
            print("That's the right letter!\n")
            pass
        elif(user=='e'):
            lettersGuessed[6]=lettersGuessed[5]
            lettersGuessed[5]='e'
            print("That's the right letter!\n")
            pass
        elif(user=='r'):
            lettersGuessed[6]=lettersGuessed[6]
            lettersGuessed[6]='r'
            print("That's the right letter!\n")
            pass
        else:
            print("That's not a missing Letter, try again...\n")
    i=0            
    while i<7:
        print("Attempt number {0}/6".format(i))
        returnstring=getGuessedWord(secretWord, lettersGuessed)
        print("Available letters:")
        usableLetters=getAvailableLetters(lettersGuessed)
        lettersGuessed[i]=input("Try and Guess... \n")
        user=lettersGuessed[i].lower()
        if len(user)!=1:
            print("Please only type in a single letter\n")
            continue
        else:
            pass
        if not user in usableLetters:
            print("That letter's been used, try again...\n")
            continue
        else:
            pass
        Answer(user)
        check=isWordGuessed(secretWord, lettersGuessed)
        i+=1
        
    if(check == True):
            print("You guessed the word!")
            print("The word was 'monster'!")
    else:
            print("Oof! You lose!")