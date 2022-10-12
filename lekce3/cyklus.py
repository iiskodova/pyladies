# name = input('Jaké je tvoje křestní jméno? ')
# surname = input('Jaké je tvoje příjmení? ')
# print(name[0].upper() + surname[0].upper()

slovo = input('řekni něco: ')
písmeno = int(input('kolikáté písmeno chceš vyměnit? '))
nové = input('a jaké je nové písmeno? ')

print('nové slovo:')
print(slovo[:písmeno] + nové + slovo[písmeno:])