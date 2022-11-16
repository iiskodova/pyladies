class Cat:
    def __init__(self, name):
        self.lives = 9
        self.name = name

    def __str__(self):
        return f'<Kitten named {self.name}>'

    def meow(self):
        print(f'{self.name}: Meow!')

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False

    def lose_life(self):
        if self.is_alive():
            self.lives -= 1
            print(self.lives)
        else:
            print(f'{self.name} is dead!')

    def eat(self, food):
        if self.is_alive():
            if food == 'fish' and self.lives < 9:
                self.lives += 1
                print(f'{self.name} got new life, she now has {self.lives}')
            else:
                print(f'{self.name} is not hungry, but the lives are still {self.lives}')
        else:
            print(f'{self.name} is dead, she cant eat anymore :(')

simba = Cat('Simba')
simba.meow()
print(simba.lives)
simba.lose_life()
simba.lose_life()
simba.eat('fish')
print(simba)
