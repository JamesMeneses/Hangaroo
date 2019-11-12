import random, sys
word_bank=["rectifier","bazinga","kalamazoo","ansatz","cloaca","gluten"]
guess_word=[]
secret_word=random.choice(word_bank)
length_word=len(secret_word)
letter_store=[]
alphabet="abcdefghijklmnopqrstuvwxyz"