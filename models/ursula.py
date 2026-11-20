from ursina import *
from models.base.player import Player
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor
from models.makarov import Makarov
from models.makarov_magazine import MakarovMagazine

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
        makarov = Makarov(magazine=makarov_magazine)

        self.speed=SPEED
        self.max_hp = MAX_HP
        self.hp = MAX_HP
        self.weapon_gun_fire = makarov 

        if self.weapon_gun_fire:
            self.weapon_gun_fire.idle()


    def manualRack(self):
        self.weapon_gun_fire.rack()

    def shoot(self):
        self.weapon_gun_fire.shoot()
        self.weapon_gun_fire.magazine.printQuantity()

    def changeMagazine(self, magazine):
        self.weapon_gun_fire.changeMagazine(magazine=magazine)

    def checkChumber(self):
        self.weapon_gun_fire.checkChumber() 

    def checkMagazine(self):
        self.weapon_gun_fire.checkMagazine()

    def aim(self):
        self.weapon_gun_fire.aim()
