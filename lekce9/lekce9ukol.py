import random

class Character:
    def __init__(self, type):
        self.lives = 100
        self.type = type

    def __str__(self):
        return f'Character type{self.type}'

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False

    def damage(self, weapon):
        if self.is_alive():
            if weapon == 'spell':
                self.lives -= 5
                print(f'{self.type} lost 5 lives, he has {self.lives} now!')
            if weapon == 'sword':
                self.lives -= 4
                print(f'{self.type} lost 4 lives, he has {self.lives} now!')
        else:
            print(f'{self.type} is dead!')

    def potion(self):
        if self.is_alive():
            pot = ['small potion', 'big potion', 'poison']
            potion = random.choice(pot)
            if potion == 'small potion':
                self.lives += 5
                print(f'{self.type} drank small potion and has {self.lives} now!')
            if potion == 'big potion':
                self.lives += 10
                print(f'{self.type} drank big potion and has {self.lives} now!')
            if potion == 'poison':
                self.lives -= 3
                print(f'{self.type} drank poison and has {self.lives} now!')
        else:
            print(f'{self.type} is dead!')

class Sorceress(Character):
    def damage(self, weapon):
        if self.is_alive():
            if weapon == 'spell':
                self.lives -= 1
                print(f'{self.type} lost 1 live, she has {self.lives} now!')
            if weapon == 'sword':
                self.lives -= 5
                print(f'{self.type} lost 4 lives, she has {self.lives} now!')
        else:
            print(f'{self.type} is dead!')

    def battle_stance(self):
        print(f'{self.type} eyes glow with yellow light as she levitates a fireball in her hand')

class Barbar(Character):
    def __init__(self, type):
        self.lives = 100
        self.type = type
        type = type.upper()
        super().__init__(type)

    def battle_stance(self):
        print(f'{self.type} clashes his swords and roars')


mage = Sorceress('Mage')
conan = Barbar('warrior')
mage.battle_stance()
conan.battle_stance()
mage.damage('spell')
conan.damage('spell')
mage.potion()
mage.damage('sword')
conan.damage('sword')
conan.potion()
mage.potion()
