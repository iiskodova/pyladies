import random

words = ['klášter', 'makovice', 'slunečník', 'plejtvák']

def hangman():
    word = random.choice(words)
    word_letters = set(word) #písmena vybraného slova
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #hádaná písmena

    user_letter = input('Hádej písmeno: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('Toto písmeno jsi už zkoušel.')
    else:
        print('Neplatný vstup. Zadávej jen písmena.')
