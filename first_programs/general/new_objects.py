class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='', age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    def speak(self):
        print(f'My name is {self.name}, and i am {self.age} years old')


player1 = PlayerCharacter('Carl', 44)
player2 = PlayerCharacter('Tommy', 23)
player2.attack = 44

print(player1.run('hello'))
print(player2.shout())
