
MAX_HP=100
SPEED=2
JUMP_HEIGHT=0 # no jump
MAX_ITEM_INVENTORY=3

class Player():
    def __init__(self):
        self.hp = MAX_HP
        self.speed = SPEED
        self.y=-0.5
        self.jump_height=JUMP_HEIGHT
        self.cursor.visible = False
        self.weapon_gun_fire = None
        self.weapon_melee =  None
        self.inventory = [0] 

    def update(self):
        print(f"Update state")

    def takeDamage(self, ammount):
        self.hp -= ammount

    def addItemInventory(self, slot, ammount):
        self.inventory[slot] += ammount

    def removeItemInventory(self, slot, ammount):
        self.inventory[slot] -= ammount
        if self.inventory[slot] < 0:
            self.inventory[slot] = 0

