
class GunFire():
    def __init__(self, magazine):

        self.magazine = magazine 
        self.chamber = [False] 

    def rack(self):
        if self.magazine.isEmpty():
            print(f"No ammo!")
            self.chamber[0] = False 
        else: 
            print(f"Rack gun!")
            self.magazine.removeAmmo()
            self.chamber[0] = True
        
    def shoot(self):
        if self.chamber[0]:
            print(f"Shoot!")
            self.rack()
        else: 
            print(f"Gun not bullet in chamber")

    def addMagazine(self, magazine):
        self.magazine = magazine

    def removeMagazine(self):
        self.magazine = None

    def printHasBulletChamber(self):
        print(f"Bullet in chumber: {self.chamber[0]}")

    def printQuantityMagazine(self):
        self.magazine.printQuantity()

