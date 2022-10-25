mountains = {
    'Kangchenjunga': [8586, 28162],
    'Lhotse': [8516, 27932],
    'Makalu': [8485, 27831],
    'Nanga Parbat': [8126, 26653],
    'Annapurna I': [8091, 26538],
    }

print('Toto je 5 hor s pěknými jmény: ')
for key in mountains:
    print(key)
print()

print('A toto jsou jejich nadmořské výšky: ')
for value in mountains.values():
    print(value[0], 'm n. m.')
print()

print('Někteří lidé radši měří ve stopách: ')
for value in mountains.values():
    print(value[1], 'ft')
print()

print('Tady to máme pěkně přehledně: ')
for key, value in sorted(mountains.items()):
    print(key, ' má ', value[0], ' metrů, což je', value[1], 'stop.')

