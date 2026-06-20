import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,x,y, image_surface):
        super().__init__()

        self.image = image_surface
        self.rect = self.image.get_rect()

        self.x = float(x)
        self.y = float(y)

        self.rect.topleft = (int(self.x),int(self.y))

    def update(self,delta_time):
        pass

    def post_update(self):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
