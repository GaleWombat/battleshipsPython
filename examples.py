
import pygame



def main():
    pygame.init()

    screen = pygame.display.set_mode((480,360))
    pygame.display.set_caption("First steps")
    points = [(20,20),(300,300)]
    color = (100,30,150)
    screen.fill(color)
    pygame.draw.circle(screen, (1,60,1), (240,180), 100, 0)
    pygame.display.update()
    clock = pygame.time.Clock()

    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            # if event == pygame.QUIT :
                print "Quitting..."
                run = False
        msElapsed = clock.tick(30)
        update_points(points,screen)

def update_points(points,screen):
    point1x = points[0][0]
    point1y = points[0][1]
    points[0]=(point1x+1,point1y+2)
    point2x = points[1][0]
    point2y = points[1][1]
    points[1]=(240,point2y-2)
    pygame.draw.circle(screen, (0,0,0), points[0], 1, 0)
    pygame.draw.circle(screen, (255,244,233), points[1], 1, 0)
    pygame.display.update()

if __name__=="__main__":
    main()