

class Magazine():
    def __init__(self, quantity, max_ammo):
        self.quantity = quantity 
        self.max_ammo = max_ammo 

    def addAmmo(self, ammount):
        if not self.isFull():
            if ammount <= self.max_ammo:
                self.quantity += ammount 
                self.printQuantity()

    def removeAmmo(self):
        if not self.isEmpty():
            self.quantity -= 1
            self.printQuantity()

    def hasAmmo(self):
        if self.quantity == 0:
            return False
        elif self.quantity > 0:
            return True

    def isFull(self):
        if self.quantity == self.max_ammo:
            return True

    def isEmpty(self):
        if self.quantity == 0:
            return True

    def printQuantity(self):
        print(f"Ammo: {self.quantity}")

