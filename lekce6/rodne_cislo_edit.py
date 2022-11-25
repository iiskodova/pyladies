def format_check(rodne_cislo):
    numbers = rodne_cislo[:6] + rodne_cislo[7:]
    if not numbers.isdigit():
        print('zadej jen čísla a lomítko')
        return False
    if not int(numbers) % 11 == 0:
        print('rodné číslo není platné')
        return False
    if not len(rodne_cislo) == 11:
        print('zadané číslo bylo moc krátké nebo dlouhé')
        return False
    if not rodne_cislo[6] == '/':
        print('chybí lomítko')
        return False
    else:
        print('Rodné číslo je v pořádku')
        return True

def gender_check(rodne_cislo):
    if int(rodne_cislo[2]) >= 5:
        return 'žena'
    else:
        return 'muž'

def birth_date(rodne_cislo):
    if int(rodne_cislo[2]) >= 5:
        month = str(int(rodne_cislo[2]) - 5) + rodne_cislo[3]
    else:
        month = rodne_cislo[2:4]

    day = rodne_cislo[4:6]
    year = rodne_cislo[0:2]
    return(day, month, year)


if __name__ == "__main__":
    while True:
        rodne_cislo = input('Napiš své rodné číslo ve formátu xxxxxx/xxxx: ')
        if not format_check(rodne_cislo) is True:
            continue
        else:
            break
    print(gender_check(rodne_cislo))
    print(birth_date(rodne_cislo))
