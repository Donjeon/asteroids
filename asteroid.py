import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):

        """
        self.x = x
        self.y = y
        self.radius = radius
        """

        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        #Small asteroid died
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #Medium asteroid died
        random_angle = random.uniform(20,50)

        split_angle1 = (random_angle)
        split_angle2 = (-random_angle)

        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS #may need to rework
        new_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        new_asteroid1.velocity = self.velocity.rotate(split_angle1)*1.2 
        
        new_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        new_asteroid2.velocity = self.velocity.rotate(split_angle2)*1.2

        