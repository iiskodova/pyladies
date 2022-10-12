from random import randrange
points = 0
while points < 21:
    print('máš celkem', points, '.')
    next = input('chceš další kartu? \nano, ne? ')
    next = next.lower()
    if next == 'ano':
        card = randrange(2,11)
        print('otočil/a jsi', card)
        points = points + card  
    elif next == 'ne':
        break
    else:
        print('piš jen ano nebo ne')

if points == 21:
    print('oko bere!')
elif points > 21:
    print('máš celkem', points)
    print('prohráváš!')
else:
    print('končíš s', points)