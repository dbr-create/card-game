import pygame
from . import entity 

class GameObject(entity.Entity):
    def __init__(self,name,description,asset,x,y):

        self.asset = pygame.image.load("assets/objects/" + asset).convert_alpha()

        super().__init__(x,y,self.asset)

        self.name = name
        self.description = description
    def post_update(self):
        super().post_update()
                    

    