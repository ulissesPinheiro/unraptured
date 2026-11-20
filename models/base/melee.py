class Weapon():
    def __init__(self, damage):
        self.damage = damage

    def atack(self):
        print(f"Melee atack: {self.damage}")
