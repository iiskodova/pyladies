herni_pole = '--------------------'

def ukaz_pole(herni_pole):
    print(herni_pole)
ukaz_pole(herni_pole)


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
        pozice = input('Napiš číslo pole v rozmetí 1-20, na které chceš umístit symbol: ')
        if not pozice.isnumeric():
            print('zadej číselnou hodnotu pole od 1 do 20: ')
            return False
        elif pozice not in range(1,21):
            print('zadej číselnou hodnotu pole od 1 do 20: ')
            return False
        elif herni_pole[pozice] != '-':
            print('toto pole je již zabrané, vyber si jiné: ')
            return False
        else:
            return True
print(tah_hrace())
        

# def seznam(herni_pole):
#     seznam_tahu = {}
#     i = 0
#     for poz in range(0, 21):
#         seznam_tahu[]
