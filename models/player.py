from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, position=(0,0,3),scale=(1,0.8,1)):
        super().__init__(
            model="cube",
            scale=scale,
            position=position
        )
        self.speed=2
        self.jump_height=0
        self.cursor.visible = False
        self.max_hp = 100
        self.hp = 100

        self.damage_overlay = Entity(
                parent=camera.ui,
                model='quad',
                scale=(2, 2),
                color=color.rgba(200, 0, 0, 0),
                z=-10
        )

    def take_damage(self, ammount):
        self.hp -= ammount
        print(f"The player take damage! hp actual: {self.hp}/{self.max_hp}")

        invoke(self.reset_overlay, delay=0.15)


        if self.hp <= 0:
            print("Player die - Game Over")
            application.quit()

    def reset_overlay(self):
        self.damage_overlay.color = color.rgba(200, 0, 0, 0)
        
