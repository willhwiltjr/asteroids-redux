# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
from player import *


pygame.init()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    black =(0,0,0,255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
