import random
from move import tah
from ai import tah_pocitace

def vyhodnot(herni_pole):
    if 'xxx' in herni_pole:
        return 'x'
    elif 'ooo' in herni_pole:
        return 'o'
    elif '-' in herni_pole:
        return '-'
    else:
        return '!'

def tah_hrace(herni_pole, player_symbol):
    while True:
        try:
            #try používám když očekávám konkrétní chybu
            pozice = int(input('Napiš číslo pole v rozpetí 0-19, na které chceš umístit symbol: '))
        except ValueError:
            continue

        if pozice < 0 or pozice > 19:
            print('zadej číselnou hodnotu pole od 0 do 19: ')

        elif herni_pole[pozice] != '-':
            print('toto pole je již zabrané, vyber si jiné: ')

        else:
            return tah(herni_pole, pozice, player_symbol)

def piskvorky1d():
    herni_pole = '--------------------'
    player_symbol = ''
    while True:
        player_symbol = input('Vyber si jestli chceš znak x nebo o: ')
        if player_symbol == 'x' or player_symbol == 'o':
            break
    comp_symbol = 'x' if player_symbol == 'o' else 'o'
    while True:
        herni_pole = tah_hrace(herni_pole, player_symbol)
        kontrola = vyhodnot(herni_pole)
        if kontrola == player_symbol:
            print('vyhrál jsi!')
            break
        if kontrola == '!':
            print('remíza!')
            break
        print('člověk', herni_pole)
        herni_pole = tah_pocitace(herni_pole, comp_symbol)
        kontrola = vyhodnot(herni_pole)
        if kontrola == comp_symbol:
            print('vyhrál počítač')
            break
        if kontrola == '!':
            print('remíza!')
            break
        print('pc', herni_pole)
