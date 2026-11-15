from ursina import *
from models.char import Char
from ursina.prefabs.first_person_controller import FirstPersonController

SPEED=2
MAX_HP=100


class Player(FirstPersonController, Char):
    def __init__(self, position_ref=0, scale_ref=1):
        super().__init__(
            model="cube",
            scale=scale_ref,
            position=position_ref
        )
        # correct hight palyer 2 camere set meter and short to 2.5
        self.y=-0.5
        self.speed=2
        self.jump_height=0
        self.cursor.visible = False
        self.max_hp = MAX_HP
        self.hp = MAX_HP

    def take_damage(self, ammount):
        self.hp -= ammount
        print(f"The player take damage! hp actual: {self.hp}/{self.max_hp}")


        if self.hp <= 0:
            print("Player die - Game Over")
            application.quit()

       
