rodne_cislo = ''

def format_check():
    while True:
        global rodne_cislo 
        rodne_cislo = input('Napiš své rodné číslo ve formátu xxxxxx/xxxx: ')
        try:
            if len(rodne_cislo) == 11:
                if rodne_cislo[6] == '/':
                    numbers = rodne_cislo[:6] + rodne_cislo[7:]
                    if int(numbers)%11 == 0:
                        return int(numbers)
        except ValueError:
            print('Zkus to znovu!')
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
