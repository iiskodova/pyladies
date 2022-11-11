import random

def tah_pocitace(herni_pole, comp_symbol):
    while True:
        pozice = random.randint(0, 19)
        if herni_pole[pozice] == '-':
            return tah(herni_pole, pozice, comp_symbol)
        if '-' not in herni_pole:
            break