import pygame

class Environment:
    def __init__(self,background):
        self.background = "assets/" + background
    def render_background(self,screen):
        background = pygame.image.load(self.background).convert()
        screen.blit(background,(0,0))
        pygame.display.flip()
