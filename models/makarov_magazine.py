from models.base.magazine import Magazine

MAX_AMMO = 8

class MakarovMagazine(Magazine):
    def __init__(self):
        super().__init__(
                    quantity = 0,
                    max_ammo = MAX_AMMO
                )
