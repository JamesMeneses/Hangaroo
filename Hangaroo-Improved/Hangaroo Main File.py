from Secret import prepare_secret_word
from guesser import guessing

def Hangaroo():
    print('Welcome to Hangaroo!\n')
    print('Would you like to play this godforsaken game?\n')
    while True:
        choice=input('Yes or No? ').lower()
        if choice=='yes' or choice=='y':
            print('coolbeans\n')
            break
        elif choice=='no' or choice=='n':
            sys.exit('Lol why even try running this thing????')
        else:
            print("It's just a yes or no question. Do it again.")
            continue


if __name__ == "__main__":
    Hangaroo()
    prepare_secret_word()
    guessing()