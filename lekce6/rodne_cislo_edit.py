def format_check():
    numbers = rodne_cislo[:6] + rodne_cislo[7:]
    try:
        if int(numbers)%11 == 0:
            return
    except ValueError:
        print('zadané číslo není dělitelné 11')
format_check()

def gender_check():
    if int(rodne_cislo[2]) >= 5:
        return 'žena'
    else:
        return 'muž'
print(gender_check())

def birth_date():
    if int(rodne_cislo[2]) >= 5:
        month = str(int(rodne_cislo[2]) - 5) + rodne_cislo[3]
    else:
        month = rodne_cislo[2:4]

    day = rodne_cislo[4:6]
    year = rodne_cislo[0:2]
    return(day, month, year)
print(birth_date())


if __name__ == "__main__":
    while True:
        rodne_cislo = input('Napiš své rodné číslo ve formátu xxxxxx/xxxx: ')
        if len(rodne_cislo) == 11:
            print('délka je správně')
        else:
            print('zadané číslo bylo moc krátké')
            continue
        if rodne_cislo[6] == '/':
            print('lomítko je správně')
        else:
            print('v zadaném čísle chybí lomítko')
        format_check()
        gender_check()
        birth_date()

