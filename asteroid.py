import pygame
from circleshape import * 
from constants import *
import random 

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0,0)
        
        if Asteroid.containers is not None: 
            for container in Asteroid.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255) ,(self.position.x, self.position.y), self.radius, width = 2 )

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
        self.kill() 
        angle = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else: 
            neg_vector = self.velocity.rotate(-angle)
            pos_vector = self.velocity.rotate(angle) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS 
            aster_left = Asteroid(self.position.x, self.position.y, new_radius) 
            aster_left.velocity = neg_vector * 1.5
            aster_right = Asteroid(self.position.x, self.position.y, new_radius) 
            aster_right.velocity = pos_vector *1.5
