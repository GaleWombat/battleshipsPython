import pygame
import time
import os

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
background_color = (85,85,236)

def main():
        pygame.init()

        screen = pygame.display.set_mode((600,480))
        pygame.display.set_caption("BATTLESHIPS")
        screen.fill(background_color)

        mouse = pygame.mouse.get_pos()
        menu(screen, mouse)
        pygame.display.quit()
    
    
        

def menu(screen,mouse):

        # setting up a menu content

        title_font = pygame.font.SysFont("monospace", 48)
        title = title_font.render("BATTLESHIPS", 4, black)
        buttons_font = pygame.font.SysFont("monospace", 18)
        play_button = buttons_font.render('PLAY', 1 ,black)
        play_focus = buttons_font.render("PLAY", 1, white)
        leaderboard_button = buttons_font.render('LEADERBOARD',1,black)
        leaderboard_focus = buttons_font.render('LEADERBOARD',1,white)
        screen.blit(title, (145, 80))

        # play button drawing

        pygame.draw.rect(screen, red, (230,180,130,40))
        screen.blit(play_button, (275, 190))

        # leaderboard button drawing

        pygame.draw.rect(screen, red, (230,230,130,40))
        screen.blit(leaderboard_button, (235, 240))

        run_menu = True
        while run_menu:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print "Quitting..."
                                run_menu = False
                        if event.type == pygame.MOUSEMOTION:
                                x,y = event.pos
                                if(x>230 and x<230+130 and y > 180 and y < 220): screen.blit(play_focus, (275, 190))
                                else:
                                        screen.blit(play_button, (275, 190))
                                if(x>230 and x<230+130 and y > 230 and y < 270): screen.blit(leaderboard_focus, (235, 240))
                                else:
                                        screen.blit(leaderboard_button, (235, 240))

                        if event.type == pygame.MOUSEBUTTONDOWN:
                                x,y = event.pos
                                if(x>230 and x<230+130 and y > 180 and y < 220): 
                                        print "play button clicked!"
                                        pygame.display.iconify()
                                        os.system("python game.py")
                                        run_menu = False
                                if(x>230 and x<230+130 and y > 230 and y < 270): print "leaderboard button clicked!"
               
                pygame.display.update()
        pygame.display.quit()
                

if __name__=="__main__":
    main()