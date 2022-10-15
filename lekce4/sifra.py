while True:
    plaintext = input('vstupní text: ')
    if any(char.isdigit() for char in plaintext):
        print('zadej pouze textový vstup')
        continue
    else:
        break

while True:
    try:
        key = int(input('posun míst o: '))
    except ValueError:
        print('zadej pouze celé kladné číslo')
        continue
    else:
        break
    
key = int(key)

cipher = ''
for i in plaintext:
    if ord(i) == 32 or ord(i) == 9:
        ciph = ord(i)
    elif i.islower():
        ciph = ord(i) + key
        if ciph > 122:
            ciph = (ciph - 122) + 96
    else:
        ciph = ord(i) + key
        if ciph > 90:
            ciph = (ciph - 90) + 64
    cipher = cipher + chr(ciph)

print(cipher)
