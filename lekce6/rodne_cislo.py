rodne_cislo = input('Napiš své rodné číslo ve formátu xxxxxx/xxxx: ')

def format_check():
    for i in range(0, len(rodne_cislo)): 
        if i == 6 and rodne_cislo[i] =='/': 
            return True
        if not rodne_cislo[i].isdigit(): 
            return False
print(format_check())

def len_check():     
    rc = []
    for i in rodne_cislo:
        cisla = i.split()
        if i.isdigit():
            rc.append(i)
    if len(rc) == 10:
        return True
    else:
        return False

print(len_check())

def divisibility():
    if (int(rodne_cislo[0:6]) + int(rodne_cislo[7:11]))%11 == 0:
        return True
    else:
        return False

print(divisibility())

def gender_check():
    gender = ''
    if int(rodne_cislo[2]) >= 5:
        gender = 'žena'
        return gender
    
    else:
        gender = 'muž'
        return gender
print(gender_check())

def birth_date():
    month = []
    if int(rodne_cislo[2]) >= 5:
        month = str(int(rodne_cislo[2]) - 5) + rodne_cislo[3]
    else:
        month = rodne_cislo[2:4]

    day = rodne_cislo[4:6]
    year = rodne_cislo[0:2]
    return(day, month, year)


print(birth_date())
