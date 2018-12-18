from random import randint

class Bot:
    def __init__(self, shotboard):
        self.ships = []
        self.shotboard = shotboard
        self.shotPositions = []
    
    def addShipPosition(self,x,y):
        self.ships.append([x,y])

    def isShipPosition(self,x,y):
        if([x,y] in self.ships): return True
        return False

    def fire(self):
        if(len(self.shotPositions) == 100): return None
        fire_x = randint(0,9)
        fire_y = randint(0,9)
        print "fire at {0}, {1}".format(fire_x,fire_y)
        while([fire_x,fire_y] in self.shotPositions):
            fire_x = randint(0,9)
            fire_y = randint(0,9)
        self.shotPositions.append([fire_x,fire_y])
        is_ship_hit = self.shotboard.hit(fire_x,fire_y)
        print "fire!"
        if(is_ship_hit): self.fire()