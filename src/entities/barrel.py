import pygame
from . import game_object

class Barrel(game_object.GameObject):
    def __init__(self,name,description,asset,x,y,damage):
        super().__init__(name,description,asset,x,y)

        self.damage = damage
    def update(self,delta_time):
        self.x = self.x + (2 * delta_time)
        self.y = self.y + (2 * delta_time)
        super().post_update()
    
