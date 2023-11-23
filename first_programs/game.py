class User():
    # def __init__(self, email):
    #     self.email = email
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __int__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __int__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50)
print(hb1.run())

# wizard1 = Wizard("merlinwiz@gmail.com")
# archer1 = Archer('Robin', 200)

# print(dir(wizard1.email))

# print(isinstance(wizard1, User))

# for char in [wizard1, archer1]:
#     char.attack()
