# Napiš program který se uživatele zeptá na rodné číslo a vypíše, zda zadal rodné číslo správně:
# (a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vypíše True nebo False)
# (b) Je dělitelné jedenácti? (vypíše True nebo False)
# (c) Jaké datum narození je v čísle zakódováno? (vypíše trojici čísel – den, měsíc, rok)
# (d) Jaké pohlaví je v čísle zakódováno? (vypíše 'muž' nebo 'žena')


rodne_cislo = input('Napiš své rodné číslo ve formátu xxxxxx/xxxx: ')

try:
    val = int(rodne_cislo[0:6])
except ValueError:
    print(False)
    quit()

try:
    val = int(rodne_cislo[7:11])
except ValueError:
    print(False)
    quit()

if (int(rodne_cislo[0:6]) + int(rodne_cislo[7:11]))%11 == 0:
    print(True)
else:
    print(False)

rc = []
for i in rodne_cislo:
    cisla = i.split()
    if i.isdigit():
        rc.append(i)

if len(rc) == 10:
    print(True)
else:
    print(False)

if len(rodne_cislo) == 11 and rodne_cislo[6] == '/' :
    print(True)
else:
    print(False)


if int(rodne_cislo[2]) >= 5:
    print('žena')
else:
    print('muž')

mesic = []
if int(rodne_cislo[2]) >= 5:
    mesic = str(int(rodne_cislo[2]) - 5) + rodne_cislo[3]
else:
    mesic = rodne_cislo[2:4]

den = rodne_cislo[4:6]
rok = rodne_cislo[0:2]
print(den, mesic, rok)
