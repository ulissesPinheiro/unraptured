
from ursina import *
from models.base.gun_fire import GunFire 
from direct.actor.Actor import Actor


DAMAGE = 5 
MODEL = "assets/models/makarov.glb"


class Makarov(GunFire):
    def __init__(self, magazine):
        GunFire.__init__(self,magazine=magazine)
        self.name = 'Makarov'
        self.damage = DAMAGE 

        self.actor = Actor(MODEL)
        self.actor.reparentTo(camera)

    def shoot(self):
        GunFire.shoot(self)
        self.actor.play('shoot')

    def idle(self):
        self.actor.loop('idle')

    def rack(self):
        GunFire.rack(self)
        self.actor.play('rack')

    def changeMagazine(self, magazine):
        GunFire.removeMagazine(self)
        GunFire.addMagazine(self, magazine=magazine)
        self.actor.play('magazine')

    def checkChumber(self):
        GunFire.printHasBulletChamber(self) 

    def aim(self):
        self.actor.play('aim')

    def checkMagazine(self):
        GunFire.printQuantityMagazine(self)

