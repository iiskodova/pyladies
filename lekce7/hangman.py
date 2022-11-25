import random
from obrazky import obrazek1, obrazek2, obrazek3, obrazek4, obrazek5, obrazek6, obrazek7, obrazek8, obrazek9
seznam_slov = ['klášter', 'makovice', 'slunečník', 'plejtvák']
slovo = ''
tajenka = ''
tah_hráče = ''

#zeptá se po první hře zda chce uživatel hrát další
def play_loop():
    play_game = input('Chceš hrát znovu? a = ano, n = ne\n')
    play_game.lower()
    while play_game not in ['a', 'n']:
        play_game = input('Chceš hrát znovu? a = ano, n = ne\n')
    if play_game == 'a':
        hangman()
    elif play_game == 'n':
        print('Díky za hru!')
        exit()

#převede náhodně vybrané slovo na podtržítka
def zadání():
    global tajenka
    slovo = random.choice(seznam_slov)
    délka = len(slovo)
    tajenka = délka * '_'
    return tajenka

#vyžádá si písmeno od hráče a zkontroluje vstup
def tah():
    while True:
        tah_hráče = input('Zadej písmeno: ')
        if len(tah_hráče) == 1 and tah_hráče.isalpha():
            return tah_hráče
        else:
            print('Zadej jen jedno písmeno prosím')


#vyhodnotí zda hádané písmeno je v tajném slově, případně započte chybný pokus a vrátí šibenici
def vyhodnocení():
    counter = 0
    if '_' not in tajenka:
        print('vyhrál jsi!')
    elif tah_hráče in slovo:
        return tajenka[:tah_hráče] + tah_hráče + tajenka[tah_hráče:]
    else:
        counter += 1
        print('toto písmeno ve slově není')
        if counter == 1:
            print(obrazek2())
        if counter == 2:
            print(obrazek3())
        if counter == 3:
            print(obrazek4())
        if counter == 4:
            print(obrazek5())
        if counter == 5:
            print(obrazek6())
        if counter == 6:
            print(obrazek7())
        if counter == 7:
            print(obrazek8())
        if counter == 8:
            print(obrazek9())
            print('prohrál jsi!')

def hangman():
    print('ŠIBENICE')
    print(obrazek1())
    print(zadání())
    print(tah())
    print(vyhodnocení())
    print(play_loop())



if __name__ == "__main__":
    hangman()
