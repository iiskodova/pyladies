from random import randrange
def dice_throw():
    return randrange(1, 6), randrange(1, 6)
a, b = dice_throw()
print(f'Hodila jsi čísla: {a} a {b}')
