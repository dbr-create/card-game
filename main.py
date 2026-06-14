import pygame
import environment

pygame.init()

WIDTH, HEIGHT = 480,270
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.SCALED)
pygame.display.set_caption("card castle")

curr_environment = environment.Environment("sunny_day.png")
curr_environment.render_background(screen)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
