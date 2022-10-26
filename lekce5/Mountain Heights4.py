mountains = {
    'Kangchenjunga': {'elevation': [8586, 28169], 'range': 'Himálaj'},
    'Lhotse': {'elevation': [8516, 27932], 'range': 'Himálaj'},
    'Makalu': {'elevation': [8485, 27831], 'range': 'Himálaj'},
    'Nanga Parbat': {'elevation' :[8126, 26653], 'range': 'Himálaj'},
    'Annapurna I': {'elevation': [8091, 26538], 'range': 'Himálaj'}
    }

print('Toto je 5 hor s pěknými jmény: ')
for key in mountains:
    print(key)
print()

print('A toto jsou jejich nadmořské výšky: ')
for key in mountains:
    e = mountains[key]['elevation']
    print(e[0])
print()

print('Hory patří do těchto pohoří: ')
for key in mountains:
    r = mountains[key]['range']
    print(r)
print()

print('Tady to máme pěkně přehledně: ')
for key, value in sorted(mountains.items()):
    for k in mountains:
        e = mountains[key]['elevation']
    for k in mountains:
        r = mountains[key]['range']
    print(key, ' má ', e[0], ' metrů a patří do pohoří', r)

