import pygame

class Room():
    def __init__(self,x,y,asset):
        self.asset = pygame.image.load("assets/" + asset).convert_alpha()
    def draw(self,screen):
        screen.blit(self.asset,(0,0))