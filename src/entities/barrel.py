import pygame
from . import game_object

class Barrel(game_object.GameObject):
    def __init__(self,name,description,asset,x,y,damage):
        super().__init__(name,description,asset,x,y)

        self.damage = damage
    def update(self,delta_time):
        if self.velocity.length() > 0:
            if self.velocity.length() > self.speed:
                self.velocity.scale_to_length(self.speed)
            if self.velocity.length() < 0.1:
                self.velocity = pygame.Vector2(float(0),float(0))
            else:
                temp = pygame.Vector2(self.velocity)
                temp.scale_to_length(self.drag)
                self.velocity = self.velocity - temp

        self.position = self.position + (self.velocity * delta_time)
        super().post_update()
    def use(self,**kwargs):
        self.velocity = -(self.position - pygame.Vector2(kwargs['x'],kwargs['y']))
