from Monster import Monster

class Dragon(Monster):
    def __init__(self, name, health):

        super().__init__(name, health)

    def breathe_fire(self):
        print(f"{self.name} breathes a huge fireball! FWOOSH!")

        return 20
    

    def take_damage(self, amount):

        print("This is override method")
        self.health -= (amount+10)