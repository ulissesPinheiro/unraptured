
class GunFire():
    def __init__(self, magazine):

        self.magazine = magazine 
        self.chambered = False 


    def _feed(self):
        if self.magazine is not None and not self.magazine.isEmpty():
            self.magazine.removeAmmo()
            self.chambered = True
        else:
            self.chambered = False

    def rack(self):
        self._feed()


    def shoot(self):
        if not self.chambered:
            return False
        
        self.chambered = False
        self._feed()
        return True
        

    def addMagazine(self, magazine):
        self.magazine = magazine

    def removeMagazine(self):
        bullets = self.getQuantityMagazineBullets()
        self.magazine = None
        return bullets

    def hasBulletChamber(self):
        return self.chambered
   
    def printHasBulletChamber(self):
        print(f"Bullet in chumber: {self.hasBulletChamber()}")

    def getQuantityMagazineBullets(self):
        return self.magazine.quantity if self.magazine else 0

    def printQuantityMagazine(self):
        self.magazine.printQuantity()

