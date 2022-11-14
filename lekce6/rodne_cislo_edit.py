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
            numbers = rodne_cislo[:6] + rodne_cislo[7:]
            if numbers.isdigit():
                print('čísla OK')
            if not numbers.isdigit():
                print('zadej jen čísla a lomítko')
                continue
            if int(numbers) % 11 == 0:
                print('rodné číslo je v pořádku')
            else:
                print('rodné číslo není platné')
                continue
            if len(rodne_cislo) == 11:
                print('délka je správně')
            else:
                print('zadané číslo bylo moc krátké nebo dlouhé')
                continue
            if rodne_cislo[6] == '/':
                print('lomítko je správně')
                break
            if not rodne_cislo[6] == '/':
                print('chybí lomítko')
                continue
print(gender_check(rodne_cislo))
print(birth_date(rodne_cislo))
