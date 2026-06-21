import pygame
from . import entity

class Player(entity.Entity):
    def __init__(self,name,description,asset,x,y):

        self.asset = pygame.image.load("assets/player/" + asset).convert_alpha()

        super().__init__(x,y,self.asset)

        self.name = name
        self.description = description


    def update(self,delta_time):
        if self.up == True:
            self.velocity.y = self.velocity.y - self.acceleration
        if self.down == True:
            self.velocity.y = self.velocity.y + self.acceleration
        if self.right == True:
            self.velocity.x = self.velocity.x + self.acceleration
        if self.left == True:
            self.velocity.x = self.velocity.x - self.acceleration
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
    def goUp(self):
        self.up = True
    def goDown(self):
        self.down = True
    def goRight(self):
        self.right = True
    def goLeft(self):
        self.left = True
    def stopUp(self):
        self.up = False
    def stopDown(self):
        self.down = False
    def stopRight(self):
        self.right = False
    def stopLeft(self):
        self.left = False