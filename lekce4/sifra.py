plaintext = input('vstupní text: ')
key = (input('posun míst o: '))
if key != int:
    print(input('zadej celé číslo pro posun míst v šifře: '))
key = int(key)

length = len(plaintext)


# while #počet nových znaků je nižší než znaků ve vstupu 
# for i in plaintext:
#     #vypiš každý


# cipher = chr(ord() + key)
# print(cipher)