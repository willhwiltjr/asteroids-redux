from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y),self.radius,2)

    def update(self,dt):
        self.position+=self.velocity*dt
    
    def split(self):
        print(f"this asteroids radius is {self.radius}")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle=random.uniform(20,50)
            velo1= self.velocity.rotate(angle)*1.2
            velo2=self.velocity.rotate(-angle)*1.2
            offset = self.velocity.normalize() * (self.radius / 2)
            new_position1 = self.position + offset
            new_position2 = self.position - offset
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            new_asteroid=Asteroid(new_position1.x,new_position1.y,new_radius)
            new_asteroid2=Asteroid(new_position2.x,new_position2.y,new_radius)
            new_asteroid.velocity=velo1
            new_asteroid2.velocity=velo2
            print("New asteroid created at", new_position1)