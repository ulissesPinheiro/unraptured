from ursina import *
from models.base.item import Item
import time as pytime


MODEL="cube"

class AmmoItem(Entity, Item):
    def __init__(self, position_ref, amount=8, model_ref=MODEL)
        Entity.__init__(
                    model=model_ref,
                    position=position_ref,
                    scale=1,
                    collider="box"
                )

        self.label = 'Ammo 9mm'
        self.slot = 0
        self.name = '9mm'

    def update(self):
        self.rotation_z += 60 * time.dt


    def interact(self, player):
        player.addItemInventory(slot=self.slot, amount=self.amount)
        pring(f"Get {self.labal} x{self.amount}. in place: {self.slot}")
        destroy(self)
