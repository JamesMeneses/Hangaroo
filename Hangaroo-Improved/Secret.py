from typing import List
from bank import secret_word
from bank import guess_word
from bank import length_word

def new_word_to_guess(letters: List):
    print("Word to guess: {0}".format(" ".join(letters)))

def guesses_made(current: int, total: int):
    print("You have {0}/{1} guesses remaining.".format(current,total))
    
def prepare_secret_word():
    for character in secret_word:
        guess_word.append("*")
    print("The secret word has {0} letters".format(length_word))
    print("Please only enter a single letter from a-z, you're not allowed to cheese this\n")
    new_word_to_guess(guess_word)    