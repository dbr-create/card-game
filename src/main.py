import pygame
from core.engine import Engine

def main():
    pygame.init()

    screen_size = (480,270)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Telecenisis time")
    
    clock = pygame.time.Clock()
    
    game_engine = Engine()

    running = True

    while running:

        dt = clock.tick(60) / 1000.0

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        game_engine.update(dt)
        game_engine.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

