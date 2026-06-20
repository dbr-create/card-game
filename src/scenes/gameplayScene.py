import pygame
import entities
print("What Python can see:", dir(entities))

class GameplayScene:
    def on_enter(self):
        self.all_objects = pygame.sprite.Group()

        for i in range(2):
            barrel = entities.Barrel("name","barel","barrel.png",i*100,i*100,20)
            self.all_objects.add(barrel)
        
        self.room = entities.Room(0,0,"sunny_day.png")


    def update(self, delta_time):
        self.all_objects.update(delta_time)
    def draw(self,screen):
        self.room.draw(screen)
        self.all_objects.draw(screen)