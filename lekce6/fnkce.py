def zamen(slovo, pozice, znak):
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    slovo = zacatek + znak + konec
    return slovo
    #cokoliv napsané po return se neprovede, return ukončí fuknci

b = zamen('ahoj', 2, 'ooo')
print(b)

def obsah(a, b):
    if a <= 0 or b <= 0:
        print('Invalid number')
        return
    return a * b

b = obsah(-6, 15)
print(b)

CONST_VALUE = 99 #konstanta = capslock - znamená to nepřepisovat hodnotu této proměnné!
def foo(a):
    b10 = a * CONST_VALUE
    return b10
print(foo(10))

def delka(slovo):
    counter = 0
    for i in slovo:
        b = b + 1
    return b

print(delka('ahoj'))


def obsah_2():
    a = input('strana1: ')
    return int(a) * int(input('další vstup:'))



