import pygame
import entities
print("What Python can see:", dir(entities))

class GameplayScene:
    def on_enter(self):
        self.all_objects = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.current_object = None

        self.player = entities.Player("name","playa","player.png",100,200)
        self.all_players.add(self.player)

        for i in range(2):
            barrel = entities.Barrel("name","barel","barrel.png",i*100,i*100,20)
            self.all_objects.add(barrel)
        
        self.room = entities.Room(0,0,"sunny_day.png")
    def handle_event(self,events):
        for event in events:
            if event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.goUp()
                    if event.key == pygame.K_s:
                        self.player.goDown()
                    if event.key == pygame.K_a:
                        self.player.goLeft()
                    if event.key == pygame.K_d:
                        self.player.goRight()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.stopUp()
                    if event.key == pygame.K_s:
                        self.player.stopDown()
                    if event.key == pygame.K_a:
                        self.player.stopLeft()
                    if event.key == pygame.K_d:
                        self.player.stopRight()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for obj in self.all_objects:
                        if obj.rect.collidepoint(x,y):
                            self.current_object = obj
                if event.type == pygame.MOUSEMOTION:
                    if self.current_object != None:
                        x_mouse, y_mouse = pygame.mouse.get_pos()
                        self.current_object.use(x = x_mouse, y = y_mouse)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.current_object = None

                        

                        
    def update(self, delta_time):
        self.player.update(delta_time)
        self.all_objects.update(delta_time)
    def draw(self,screen):
        self.room.draw(screen)
        self.all_objects.draw(screen)
        self.all_players.draw(screen)