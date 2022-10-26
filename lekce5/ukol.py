zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

spravny = []
chybny = []

for i in zaznamy:
    jmena = i.split(' ')
    if jmena[0][0].isupper() and jmena[0][1:].islower() and jmena[1][0].isupper() and jmena[1][1:].islower():
        spravny.append(i)
    else:
        chybny.append(i)
    

print(spravny)
print(chybny)

for i in chybny:
    b = i.split(' ')
    krestni = b[0].capitalize()
    prijmeni = b[1].capitalize()
    spravny.append(' '.join([krestni, prijmeni]))

print(spravny)
            
