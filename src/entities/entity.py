import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,x,y, image_surface):
        super().__init__()

        self.image = image_surface
        self.rect = self.image.get_rect()

        self.position = pygame.Vector2(float(x),float(y))
        self.velocity = pygame.Vector2(float(0),float(0))
        self.acceleration = 10
        self.speed = 40
        self.drag = 0.05
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.rect.topleft = (int(self.position.x),int(self.position.y))

    def update(self,delta_time):
        pass

    def post_update(self):
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)
