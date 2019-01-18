import pygame
from random import randint
from game_components import background_color 
from game_components import comunicate_font
from game_components import focus_color

class Bot:
    """Klasa reprezentujaca przeciwnika komputerowego"""
    def __init__(self, shotboard):
        self.ships = []
        self.shotboard = shotboard
        self.shotPositions = []
    
    def addShipPosition(self,x,y):
        """Metoda dodajaca statek do listy statkow przeciwnika"""
        self.ships.append([x,y])

    def isShipPosition(self,x,y):
        """Metoda sprawdzajaca czy na danej pozycji jest statek"""
        if([x,y] in self.ships): return True
        return False

    def fire(self, screen):
        """Metoda ktora 'strzela' do planszy gracza - metoda losuje pozycje na ktora strzela dopoki nie wylosuje
        pozycji na ktora nie strzelala, a w przypadku trafienia wyswietla odpowiedni komunikat na ekranie screen
        oraz strzela raz jeszcze"""
        if(len(self.shotPositions) == 100): return None
        fire_x = randint(0,9)
        fire_y = randint(0,9)
        while([fire_x,fire_y] in self.shotPositions):
            fire_x = randint(0,9)
            fire_y = randint(0,9)
        self.shotPositions.append([fire_x,fire_y])
        is_ship_hit = self.shotboard.hit(fire_x,fire_y)
        if(is_ship_hit): 
            pygame.draw.rect(screen, background_color, (365,440,500,30))
            screen.blit(comunicate_font.render("Your ship has been hit!",1,focus_color), (390, 440))
            self.fire(screen)