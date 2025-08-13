# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import *


pygame.init()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    asteroids=pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers=updatable
    Asteroid.containers=(asteroids, updatable, drawable)
    Player.containers=(updatable, drawable)
    field=AsteroidField()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    black =(0,0,0,255)
    dt=0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        updatable.update(dt)
        for stroid in asteroids:
            if player.iscolliding(stroid):
                sys.exit("Game over!")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000



if __name__ == "__main__":
    main()
