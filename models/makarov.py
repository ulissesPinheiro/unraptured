
from ursina import *
from models.base.gun_fire import GunFire 
from direct.actor.Actor import Actor


DAMAGE = 5 
MODEL = "assets/models/makarov.glb"

BLOCKING_ANIMS = ("shoot", "rack", "chamber")

def _is_any_anim_playing(actor, anim_names=BLOCKING_ANIMS):
    for name in anim_names:
        ctrl = actor.getAnimControl(name)
        if ctrl and ctrl.isPlaying():
            return True
    return False


class Makarov(GunFire):
    def __init__(self, magazine):
        GunFire.__init__(self,magazine=magazine)
        self.name = 'Makarov'
        self.damage = DAMAGE 
        self.aim_mode = False

        self.actor = Actor(MODEL)
        self.actor.reparentTo(camera)

    def shoot(self):
        if self.aim_mode:
            if not _is_any_anim_playing(self.actor):
                if GunFire.hasBulletChamber(self):
                    GunFire.shoot(self)
                    self.actor.play('shoot')
        else:
            print(f"Cant shoot: Not aim mode")

    def idle(self):
        self.actor.loop('idle')

    def rack(self):
        if not self.aim_mode:
            GunFire.rack(self)
            self.actor.play('rack')
        else:
            print(f"Can not rack: Aim mode")

    def changeMagazine(self, magazine):
        if not self.aim_mode:
            GunFire.addMagazine(self, magazine=magazine)
            self.actor.play('change_magazine')

    def removeMagazine(self):
        return GunFire.removeMagazine(self)

    def checkChumber(self):
        if not self.aim_mode:
            GunFire.printHasBulletChamber(self) 
            self.actor.play('chamber')
        else:
            print(f"Cant check chumber: Aim mode")

    def aim(self):
        if self.aim_mode:
            self.aim_mode = False
            self.idle()
        else:
            self.aim_mode = True
            self.actor.play('aim')

    def checkMagazine(self):
        if not self.aim_mode:
            GunFire.printQuantityMagazine(self)
            self.actor.play('check_magazine')
        else:
            print(f"Cant Check magazine: Aim mode")

