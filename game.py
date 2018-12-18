import pygame
from random import randint
import game_components as gc
import opponent as bot

background_color = (85,85,236)

pygame.init()

ending_font = pygame.font.SysFont("monospace", 28)
pygame.mixer.music.load("Ride of the Valkyries.mp3")
pygame.mixer.music.play(-1)

def find_tile_in_board(board, x, y):
    for i in xrange(10):
        for j in xrange(10):
            if x in range(board.data[i][j].pos_x, board.data[i][j].pos_x+gc.tile_size) and y in range(board.data[i][j].pos_y, board.data[i][j].pos_y+gc.tile_size):
                return [i,j]
    else: return[-1,-1]

def place_ships(board,coords):
    board.ships_on_board.append(coords)
    for item in coords:
        board.place_ship_tile(item)
    print "current shhips: ",board.ships_on_board

def place_oponent_ships(board):
    generate_ship(board,4)
    generate_ship(board,3)
    generate_ship(board,3)
    generate_ship(board,2)
    generate_ship(board,2)
    generate_ship(board,2)
    generate_ship(board,1)
    generate_ship(board,1)
    generate_ship(board,1)
    generate_ship(board,1)

def place_one_ship(screen,board,size_of_ship):
    index = 0
    placed = False
    locationFounded = False
    vertical = False
    current_ship = []
    while(not placed):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord("r"):
                    print "r pressed"
                    if vertical: vertical = False
                    else: vertical = True
                if event.key == ord("c") or event.key == pygame.K_ESCAPE:
                    placed = True
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                if(x in range(board.pos_x,board.pos_x+10*gc.tile_size) and y in range(board.pos_y,board.pos_y+10*gc.tile_size)):
                    pos = find_tile_in_board(board,x,y)
                    correct = False
                    some_is_blocekd = False
                    real_size_to_draw = 0
                    for i in xrange(size_of_ship):
                        if vertical:
                            if(pos[0]+i not in range(0,10)): break
                            if(board.data[pos[0]+i][pos[1]].is_blocked()): some_is_blocekd = True
                            real_size_to_draw+=1
                        else:
                            if(pos[1]+i not in range(0,10)): break
                            if(board.data[pos[0]][pos[1]+i].is_blocked()): some_is_blocekd = True
                            real_size_to_draw+=1
                    print "real_size: ",real_size_to_draw
                    if(not some_is_blocekd and real_size_to_draw == size_of_ship): correct = True
                    if(correct):
                        board.draw_self(screen) 
                        board.draw_ship_in_placing(screen,vertical,pos[0],pos[1],real_size_to_draw,gc.available_color)
                        current_ship = []
                        if vertical:
                            for i in range(pos[0],pos[0]+real_size_to_draw):
                                current_ship.append([i,pos[1]])
                        else:
                            current_ship = []
                            for i in range(pos[1],pos[1]+real_size_to_draw):
                                current_ship.append([pos[0],i])
                        pygame.display.update()
                        print "current ship: ", current_ship
                    else:
                        board.draw_self(screen) 
                        board.draw_ship_in_placing(screen,vertical,pos[0],pos[1],real_size_to_draw,gc.hit_color)
                        pygame.display.update()                   

                else:
                    board.draw_self(screen)
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                place_ships(board,current_ship)
                board.draw_self(screen)
                pygame.display.update()
                placed = True

            

                    

def place_player_ships(screen,board):
    place_one_ship(screen,board,4)
    place_one_ship(screen,board,3)
    place_one_ship(screen,board,3)
    place_one_ship(screen,board,2)
    place_one_ship(screen,board,2)
    place_one_ship(screen,board,2)
    place_one_ship(screen,board,1)
    place_one_ship(screen,board,1)
    place_one_ship(screen,board,1)
    place_one_ship(screen,board,1)


def generate_ship(board,size_of_ship):
    ver_or_hor = randint(1,2)
    vertical = False
    if(ver_or_hor==1): vertical = True
    placed = False
    current_ship = []
    if(vertical): print "Vertical"
    else: print "Horizontal"
    shorten = 9-size_of_ship
    while(not placed):
        place_x = randint(0,(shorten if vertical else 9))
        print "place_x: ",place_x
        place_y = randint(0,(shorten if not vertical else 9))
        print "place_y: ",place_y
        while(board.data[place_x][place_y].is_blocked()):
            place_x = randint(0,((9-size_of_ship) if vertical else 9))
            place_y = randint(0,((9-size_of_ship) if not vertical else 9))
        for i in xrange(size_of_ship):
            if vertical:
                if board.data[place_x+i][place_y].is_blocked() : break
            else:
                if board.data[place_x][place_y+i].is_blocked() : break
        else:
            placed = True
    for i in xrange(size_of_ship):
        if vertical:
            current_ship.append([place_x+i,place_y])
        else:
            current_ship.append([place_x,place_y+i])
    print "ship found: ", current_ship
    place_ships(board,current_ship)

def ending(screen,victory,oponent_board_hits, player_board_hits):
    if victory:
        pygame.draw.rect(screen,gc.available_color,(355,110,300,100))
        string = ending_font.render("VICTORY",1,gc.focus_color)
    else:
        pygame.draw.rect(screen,gc.hit_color,(355,110,300,100))
        string = ending_font.render("DEFEAT",1,gc.focus_color)
    screen.blit(string, (450, 140))
    pygame.display.update()
    waiting = True
    while waiting == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_ENTER:
                    waiting = False


def main():

    screen = pygame.display.set_mode((1024,600))
    pygame.display.set_caption("BATTLESHIPS GAME")
    screen.fill(background_color)

    player_board = gc.Board(False,100,100)
    oponent_board = gc.Board(True,600,100)

    opponent = bot.Bot(player_board)
    player_board.draw_self(screen)
    oponent_board.draw_self(screen)
    pygame.display.update()

    place_oponent_ships(oponent_board)
    place_player_ships(screen,player_board)
    pygame.display.update()

    print "In game!"
    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "Quitting..."
                run = False
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                if(x in range(600,600+10*gc.tile_size) and y in range(100,100+10*gc.tile_size)):
                    pos = find_tile_in_board(oponent_board,x,y)
                    if(pos != [-1,-1]): oponent_board.draw_self(screen,pos[0],pos[1])
                                
                else:
                    player_board.draw_self(screen)
                    oponent_board.draw_self(screen)

                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if(x in range(600,600+10*gc.tile_size) and y in range(100,100+10*gc.tile_size)):
                    pos = find_tile_in_board(oponent_board,x,y)
                    if(pos != [-1,-1] and not oponent_board.data[pos[0]][pos[1]].is_hit()): 
                        is_ship_hit = oponent_board.hit(pos[0],pos[1])
                        # print "is_ship_hit: ", is_ship_hit
                        if(not is_ship_hit): opponent.fire()
                        player_board.draw_self(screen)
                        oponent_board.draw_self(screen)
                        pygame.display.update()
                        if(oponent_board.ships_on_board == []): 
                            ending(screen,True,oponent_board.ship_tiles_hitted,player_board.ship_tiles_hitted)
                            run = False
                        elif(player_board.ships_on_board == []): 
                            ending(screen,False,oponent_board.ship_tiles_hitted,player_board.ship_tiles_hitted)
                            run = False
        


if __name__=="__main__":
    main()