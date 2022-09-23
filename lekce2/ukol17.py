
from random import randrange
cislo = randrange(3)


tah_cloveka = str(input('Zadej svůj tah, kámen, nůžky nebo papír?: '))

if cislo == 0:
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'
    
print('Počítač dává: ',  tah_pocitace)

print('Ty dáváš: ', tah_cloveka)

if tah_pocitace == tah_cloveka:
    print('Plichta!')
elif tah_cloveka == 'kámen' and tah_pocitace == 'nůžky' or tah_cloveka == 'papír' and tah_pocitace == 'kámen' or tah_cloveka == 'nůžky' and tah_pocitace == 'papír':
    print('Vyhrál jsi!')
else:
    print('Vyhrál počítač!')