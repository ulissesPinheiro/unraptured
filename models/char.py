
MAX_HP=100
SPEED=2

class Char():
    def __ini__(self):
        self.hp = MAX_HP
        self.speed = SPEED

    def update(self):
        print(f"Update state")

    def take_damage(self, ammount):
        self.hp -= ammount

