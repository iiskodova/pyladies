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

def tah_hrace(herni_pole, cislo_pole, symbol):
    while True:
        pozice = '0'
        while pozice not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] or pozice == '':
            pozice = input('Napiš číslo pole, na které chceš umístit symbol: ')
            koord = seznam_tahu.get(int(pozice))
        
        if herni_pole[koord[0]] == '-':
            herni_pole[koord[0]] == symbol
            print(herni_pole)
            return herni_pole
        else:
            print('Tato pozice není volná, hrej znovu.')

# def seznam(herni_pole):
#     seznam_tahu = {}
#     i = 0
#     for poz in range(0, 21):
#         seznam_tahu[]
