
print('Toto je program na výměnu písmen.')

word = input('V jakém slově potřebuješ změnu? ')
letter = input('Kolikáté písmeno chceš změnit? pozor, počítáme od nuly! ')
if letter != int:
    letter = input('zadej prosím číselnou hodnotu: ')
letter = int(letter)
new_letter = input('A jaké je nové písmeno? ')
print('Tvoje nové slovo je: ', word[:letter], new_letter, word[letter + 1:])