
from random import randrange
cislo = randrange(3)
tah_pocitace = cislo

if cislo == 0:
    tah_pocitace = "kámen"
elif cislo == 1:
    tah_pocitace = "nůžky"
else:
    tah_pocitace = "papír"
    
print(tah_pocitace)

print()