import pygame
from player import Player 
from circleshape import CircleShape
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x: int = SCREEN_WIDTH / 2
    y: int = SCREEN_HEIGHT / 2
    player = Player(x,y)

    print(f"Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
