from random import randrange

while True:
    if 13 == randrange(100):
        print('hurá')
        break
    print('smutno')


for i in range(10):
    if i > 2 and i < 5:
        continue
    print(i)


counter = 0
while True:
    counter += 1
    if 13 == randrange(100):
        print('tak to vyšlo')
        print('trvalo to jenom', counter, 'x')
        break
    print('smutno')

print()
print('Break!')
for i in range(10):
    if i > 3 and i < 7:
        break
    print(i)

# ctrl + K, pak ctrl + C = zakomentovat
# ctrl + K, ctrl + u = odkomentovat
# alt 60 <          alt 62 > alt + f [  alt + g ]

x = 'Ahoj světe'
print(x[0]) #pozice 0 v proměnné x
print(len(x)) #délka proměnné x


name = (input 'Jaké je tvoje křestní jméno?')
surname = (input 'Jaké je tvoje příjmení?')
print(name[0], surname[0])