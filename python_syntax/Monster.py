class Monster:
    def __init__(self, name,health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount : int = 10):
        """
        args :
            amount : int monster to take damage
        """

        self.health -= amount
        print(f"{self.name} took {amount} damage!")
        print(f"It now has {self.health} health left.")