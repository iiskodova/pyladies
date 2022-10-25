# def take_second(elem):
#     return elem[1]

# zvirata = ['had', 'andulka', 'pes', 'kočka', 'rybička']
# for i in zvirata:
#     zvirata.sort(key=take_second)

# print (zvirata)

zvirata = [('a', 'had'), ('n', 'andulka'), ('e', 'pes'), ('o', 'kočka'), ('y', 'rybička')]
zvirata.sort(key=lambda a: a[0])
serazeno = []
for a, b in zvirata:
    serazeno.append(b)
print(serazeno)