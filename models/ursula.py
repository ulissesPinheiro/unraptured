from ursina import *
from models.base.player import Player
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor
from models.makarov import Makarov
from models.makarov_magazine import MakarovMagazine
import time as pytime

SPEED=2
MAX_HP=100


class Ursula(FirstPersonController, Player):
    def __init__(self, position_ref=0, scale_ref=1):
        FirstPersonController.__init__(
            self,
            model="cube",
            scale=scale_ref,
            position=position_ref
        )
        Player.__init__(self)
        makarov_magazine = MakarovMagazine()
        makarov_magazine.addAmmo(ammount=8)
        makarov = Makarov(magazine=makarov_magazine)
       
        # inventory
        self.inventory[0] = 16
        
        # camera bloble
        self.aim_time = 0
        self.sway_speed = 3.0
        self.sway_amount = 0.5

        self.weapon_gun_fire = makarov 

        if self.weapon_gun_fire:
            self.weapon_gun_fire.idle()

    def update(self):
        super().update()
        self.aim_time += time.dt

        if self.weapon_gun_fire.aim_mode:
             sway_x = math.sin(self.aim_time * self.sway_speed ) * self.sway_amount 
             sway_y = math.cos(self.aim_time * self.sway_speed * 0.7) * self.sway_amount 
            
             camera.rotation_x += sway_y * time.dt
             camera.rotation_z += sway_x * time.dt
        else:
            camera.y = lerp(camera.y, 0, time.dt * 10)

    def manualRack(self):
        self.weapon_gun_fire.rack()

    def shoot(self):
        self.weapon_gun_fire.shoot()
        self.weapon_gun_fire.magazine.printQuantity()

    def changeMagazine(self):
        makarov_magazine = MakarovMagazine()
        makarov_magazine.addAmmo(ammount=(self.inventory[0] - makarov_magazine.max_ammo))
        Player.removeItemInventory(self, slot=0, ammount=makarov_magazine.max_ammo)
        bullets_rest = self.weapon_gun_fire.removeMagazine()
        Player.addItemInventory(self, slot=0, ammount=bullets_rest)
        self.weapon_gun_fire.changeMagazine(magazine=makarov_magazine)

    def checkChumber(self):
        self.weapon_gun_fire.checkChumber() 

    def checkMagazine(self):
        self.weapon_gun_fire.checkMagazine()

    def aim(self):
        self.weapon_gun_fire.aim()
