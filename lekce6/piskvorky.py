herni_pole = '---xx---oo---'
def vyhodnot():
    if 'xxx' in herni_pole:
        print('x')
        return
    elif 'ooo' in herni_pole:
        print('o')
        return
    elif not '-' in herni_pole and not 'ooo' in herni_pole and not 'xxx' in herni_pole:
        print('!')
        return
    else:
        print('-')
        return
print(vyhodnot())

def tah(herni_pole, cislo_pole, symbol):
    zacatek = herni_pole[:cislo_pole]
    konec = herni_pole[cislo_pole + 1:]
    herni_pole = zacatek + symbol + konec
    return herni_pole
print(tah(herni_pole, 2, 'x'))


