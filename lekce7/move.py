def tah(herni_pole, cislo_pole, symbol):
    if cislo_pole == 0:
        return symbol + herni_pole[1:]
    if cislo_pole == 19:
        return herni_pole[:19] + symbol
    return herni_pole[:cislo_pole] + symbol + herni_pole[cislo_pole + 1:]
