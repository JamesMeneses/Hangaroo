import random, sys
from typing import List
print('Welcome to Hangaroo!\n')
print('Would you like to play this godforsaken game?\n')
while True:
    choice=input('Yes or No? ').lower()
    if choice=='yes' or choice=='y':
        print('Godspeed to you...\n')
        break
    elif choice=='no' or choice=='n':
        sys.exit('Lol why even try running this thing????')
    else:
        print("It's just a yes or no question. Do it again.")
        continue
    
word_bank=["rectifier","bazinga","kalamazoo","ansatz","cloaca","gluten"] #somehow get word list from .txt file
guess_word=[]
secret_word=random.choice(word_bank)
length_word=len(secret_word)
letter_store=[]
alphabet="abcdefghijklmnopqrstuvwxyz"
    
def new_word_to_guess(letters: List):
    print("Word to guess: {0}".format(" ".join(letters)))

def guesses_made(current: int, total: int):
    print("You have {0}/{1} guesses remaining.".format(current,total))
    
def prepare_secret_word():
    for character in secret_word:
        guess_word.append("-")
    print("The secret word has {0} letters".format(length_word))
    print("Please only enter a single letter from a-z, you're not allowed to cheese this\n")
    new_word_to_guess(guess_word)    

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
                if not '-' in guess_word:
                    print("The secret word is {0}!".format(secret_word))
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
                    
if __name__ == "__main__":
    prepare_secret_word()
    guessing()

