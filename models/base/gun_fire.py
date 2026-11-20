
class GunFire():
    def __init__(self, magazine):

        self.magazine = magazine 
        self.chamber = [0] 

    def rack(self):
        self.motorRack()
        

    def shoot(self):
        self.motorRack()

    def motorRack(self):
        if not self.hasBulletChamber():
            self.magazine.removeAmmo()
            self.addBulletChamber()
        else:
            if not self.magazine.isEmpty():
                self.magazine.removeAmmo()
                self.addBulletChamber()
            else:
                self.dropBulletChamber();

    def addMagazine(self, magazine):
        self.magazine = magazine

    def removeMagazine(self):
        self.magazine = None

    def addBulletChamber(self):
        self.chamber[0] = 1

    def dropBulletChamber(self):
        if self.hasBulletChamber():
            self.chamber[0] = 0

    def hasBulletChamber(self):
        if self.chamber[0] == 1:
            return True
        else:
            self.chamber[0] == 0
            return False

    def printHasBulletChamber(self):
        print(f"Bullet in chumber: {self.chamber[0]}")

    def printQuantityMagazine(self):
        self.magazine.printQuantity()

