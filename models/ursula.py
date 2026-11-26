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
        self.camera_pivot.y = 1.6
        Player.__init__(self)
        makarov_magazine = MakarovMagazine()
        makarov_magazine.addAmmo(amount=8)
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
        self.weapon_gun_fire.update()

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
        hit = self.weapon_gun_fire.shoot(ignore=(self,))
        if hit is not None:
            self.weapon_gun_fire.printQuantityMagazine()
        
    def changeMagazine(self):
        gun = self.weapon_gun_fire

        if not gun.can("reload"):
            return

        new_mag = MakarovMagazine()
        to_load = min(self.inventory[0], new_mag.max_ammo)
        new_mag.addAmmo(amount=to_load)
        self.removeItemInventory(slot=0, amount=new_mag.max_ammo)
        self.addItemInventory(slot=0, amount=gun.removeMagazine())
        gun.changeMagazine(magazine=new_mag)

    def checkChumber(self):
        self.weapon_gun_fire.checkChumber() 

    def checkMagazine(self):
        self.weapon_gun_fire.checkMagazine()

    def aim(self):
        self.weapon_gun_fire.aim()
