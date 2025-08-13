import pygame
from constants import PLAYER_RADIUS

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        # we will be using this later
        if hasattr(self, "containers"):
            for group in self.containers:
                group.add(self)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def iscolliding(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius


    def update(self, dt):
        # sub-classes must override
        pass