from ursina import camera, mouse, raycast


MAX_HP=100
SPEED=2
JUMP_HEIGHT=0 # no jump
MAX_ITEM_INVENTORY=3
INTERACT_DISTANCE=1

class Player():
    def __init__(self):
        self.hp = MAX_HP
        self.speed = SPEED
        self.jump_height=JUMP_HEIGHT
        self.cursor.visible = False
        self.weapon_gun_fire = None
        self.weapon_melee =  None
        self.inventory = [0] 
        self.death = False

        self.on_hurt = None
        self.on_death = None

    def update(self):
        print(f"Update state")

    def takeDamage(self, amount):
        if self.death:
            return

        self.hp = max(0, self.hp - amount)

        print(f"Player HP: {self.hp}")

        if self.on_hurt:
            self.on_hurt(self)

        if self.hp == 0:
            self.die()

    def die(self):
        self.death = True
        mouse.locked = False
        if self.on_death:
            self.on_death(self)

    def interact(self):
        if self.dead:
            return

        hit = raycast(camera.world_position, camera.forward,
                      distance=INTERACT_DISTANCE, ignore=(self,))
        if hit.hit and hasattr(hit.entity, "interact"):
            hit.entity.interact(self)

    def addItemInventory(self, slot, amount):
        self.inventory[slot] += amount

    def removeItemInventory(self, slot, amount):
        self.inventory[slot] -= amount
        if self.inventory[slot] < 0:
            self.inventory[slot] = 0

