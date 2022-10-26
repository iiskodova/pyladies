animals = ['dog', 'cat', 'python']
wild_animals = ['deer', 'fox', 'owl']

for a in animals:
    print(a)

animals.append('parrot')

print(len(animals))
print(animals.count('cat'))
animals.sort(reverse=True)
print(animals)
all_animals = []
all_animals.extend(wild_animals)
all_animals.extend(animals)
print(all_animals)
all_animals.clear()
all_animals = animals + all_animals

balicek = []
for barva in '♠', '♥', '♦', '♣':
    for hodnota in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        balicek.append(hodnota + barva)
print(balicek)