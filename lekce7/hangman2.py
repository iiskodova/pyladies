import random
from obrazky import display_hangman

def get_word():
    words = ['klášter', 'makovice', 'slunečník', 'plejtvák']
    word = random.choice(words)
    return word.upper()

def game(word):
    word = get_word()
    play(word)

def guess_input():
    guess = input('Zadej hádané písmeno: ').upper()
    return guess

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 0
    print('Hrajeme šibenici!')
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries < 8:
        guess = guess_input()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'Písmeno {guess} jsi už hádal.')
            elif guess not in word:
                print(f'Písmeno {guess} v hádaném slově není.')
                tries += 1
                guessed_letters.append(guess)
            else:
                print(f'Skvělé, písmeno {guess} je v hledaném slově!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True

        else:
            print('neplatný vstup')
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('Gratuluji, uhodl jsi!')
    if tries == 8:
        print('Bohužel už visíš!')

def hangman():
    word = get_word()
    play(word)
    while input('Chceš hrát znovu? (A/N): ').upper() == 'A':
        game(word)

if __name__ == '__main__':
    hangman()
