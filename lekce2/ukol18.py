

print('Odpovídej jen "ano" nebo "ne".')

šťastná = input('Jsi šťastná? ')
šťastná = šťastná.lower()

if šťastná in ['ano', 'ne']:
    print('Díky.')
else :
    print('Máš odpovídat jen "ano" nebo "ne".')
    quit()

bohatá = input('jsi bohatá? ')
bohatá = bohatá.lower()

if bohatá in ['ano', 'ne']:
    print('Díky, teď to vyhodnotíme.')
else :
    print('Máš odpovídat jen "ano" nebo "ne".')
    quit()

if šťastná == 'ano':
    if bohatá == 'ano':
        print('Gratuluji, jsi šťastná a bohatá!')
    elif bohatá == 'ne':
        print('Super že jsi šťastá, nechtěla bys i trochu šetřit?')

elif šťastná == 'ne':
    if bohatá == 'ne':
        print('To je mi líto :(')
    elif bohatá == 'ano':
        print('Zkus zajít na masáž nebo do kina')

else:
    print('nerozumím')