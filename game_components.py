import pygame

tile_size = 30
tile_basic_color = (60,60,150)
ship_color = (60,60,50)
hit_color = (255,10,10)
sink_color = (200,30,30)
miss_color = (10,30,20)
focus_color = (255,255,255)
available_color = (20,200,20)

how_many_ship_tiles = 20



class Tile:

    def __init__(self,is_oponent_tile,pos_x=0,pos_y=0,size=tile_size):
        self.is_oponent = is_oponent_tile
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.isShip = False
        self.isBlocked = False
        self.isHit = False
        self.isSunk = False 
        self.size = size

    def __str__(self):
        return str((self.pos_x,self.pos_y))

    def draw_self(self,screen,isFocus = False,color = focus_color):
        # if(color is not tile_basic_color): pygame.draw.rect(screen,focus_color,(self.pos_x,self.pos_y,self.size,self.size))
        if(isFocus): pygame.draw.rect(screen,color,(self.pos_x,self.pos_y,self.size,self.size))
        elif(self.isShip):
            if(self.isSunk):  pygame.draw.rect(screen,sink_color,(self.pos_x,self.pos_y,self.size,self.size))
            elif(self.isHit): pygame.draw.rect(screen,hit_color,(self.pos_x,self.pos_y,self.size,self.size))
            elif(not self.is_oponent): pygame.draw.rect(screen,ship_color,(self.pos_x,self.pos_y,self.size,self.size))
            else: pygame.draw.rect(screen,tile_basic_color,(self.pos_x,self.pos_y,self.size,self.size))
        else:
            if(self.isHit): pygame.draw.rect(screen,miss_color,(self.pos_x,self.pos_y,self.size,self.size)) 
            else: pygame.draw.rect(screen,tile_basic_color,(self.pos_x,self.pos_y,self.size,self.size))
        
    


    def get_pos(self):
        return (self.pos_x,self.pos_y)
    
    def update(self,new_x,new_y):
        self.pos_x = new_x
        self.pos_y = new_y
    
    def placeShip(self):
        self.isShip = True
        self.isBlocked = True
    
    def block(self):
        self.isBlocked = True

    def hit(self):
        self.isHit = True
    
    def sink(self):
        self.isSunk = True

    def is_hit(self):
        return self.isHit

    def is_ship(self):
        return self.isShip
    
    def is_blocked(self):
        return self.isBlocked

class Board:
    
    def __init__(self,is_oponent_board,pos_x = 100, pos_y = 100):
        self.is_oponent = is_oponent_board
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delta = tile_size+1
        self.data = [[None for x in xrange(10)] for x in xrange(10)]
        self.ship_tiles_placed = 0
        self.ship_tiles_hitted = 0
        self.ships_on_board = []
        curr_x = self.pos_x
        curr_y = self.pos_y
        for i in xrange(10):
            for j in xrange(10):
                tile = Tile(self.is_oponent,curr_x,curr_y)
                self.data[i][j] = tile
                curr_x += self.delta
            curr_x = self.pos_x
            curr_y += self.delta
    
    def count_ships(self):
        return self.ship_tiles_placed
    
    def draw_ship_in_placing(self,screen,vertical,start_x,start_y,size,color):
        print "start_x: ",start_x,", start_y: ",start_y,", vertical: ",vertical, ", size: ",size
        if vertical:
            for i in range(start_x,start_x+size):
                self.data[i][start_y].draw_self(screen,True,color)
        else:
            for i in range(start_y,start_y+size):
                print "in"
                self.data[start_x][i].draw_self(screen,True,color)

    def hit(self,x,y):
        isShipHitted = False
        self.data[x][y].hit()
        if self.data[x][y].is_ship():
            isShipHitted = True
            for ship in self.ships_on_board:
                try:
                    if ship.index([x,y]) != None:
                        for tile in ship:
                            if self.data[tile[0]][tile[1]].is_hit() == False: break
                        else:
                            for tile in ship:
                                self.data[tile[0]][tile[1]].sink()
                            self.ships_on_board.remove(ship)
                except ValueError:
                    pass
        return isShipHitted

    def __str__(self):
        return (str(self.data))

    def add(self,tile,x=0,y=0):
        self.data[x][y] = tile
        self.pos+=1

    def draw_self(self,screen,focus_x = -1,focus_y = -1,color = focus_color):
        for x in xrange(10):
            for y in xrange(10):
                if(self.data[x][y]!=None): self.data[x][y].draw_self(screen)
        if(focus_x != -1 and focus_y != -1): self.data[focus_x][focus_y].draw_self(screen,True,color)
    
    def place_ship_tile(self, ship_coords):
        for x in xrange(len(ship_coords)):
            self.data[ship_coords[0]][ship_coords[1]].placeShip()
            if(ship_coords[0]>0): self.data[ship_coords[0]-1][ship_coords[1]].block()
            if(ship_coords[0]<9): self.data[ship_coords[0]+1][ship_coords[1]].block()
            if(ship_coords[1]<9): self.data[ship_coords[0]][ship_coords[1]+1].block()
            if(ship_coords[1]>0): self.data[ship_coords[0]][ship_coords[1]-1].block()
            self.ship_tiles_placed+=1