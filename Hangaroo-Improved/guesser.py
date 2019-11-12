from Secret import guesses_made
from Secret import new_word_to_guess
from bank import alphabet
from bank import letter_store
from bank import secret_word
from Secret import guess_word
from bank import length_word

def guessing():
    guess_made=5
    max_guess=5
    guesses_made(guess_made, max_guess)
    while guess_made!=0:
        guess=input("Take a guess... ").lower()
        if not guess in alphabet:
            print("That ain't no letter, try again\n\n")
        elif guess in letter_store:
            print("That letter's been guessed, try again\n\n")
        else:
            letter_store.append(guess)
            if guess in secret_word:
                print("That's apparently a missing letter!\n\n")
                for i in range (0,length_word):
                    if secret_word[i]==guess:
                        guess_word[i]=guess
                if not '*' in guess_word:
                    print('The secret word is "{0}"!'.format(secret_word))
                    print("Wow epic win bro")
                    break
                new_word_to_guess(guess_word)
                guesses_made(guess_made,max_guess)
            else:
                print("Not the letter you're looking for, next letter!\n\n")
                guess_made-=1
                new_word_to_guess(guess_word)
                guesses_made(guess_made,max_guess)
                if guess_made==0:
                    print("The secret word was {0}, you just took the L.".format(secret_word))