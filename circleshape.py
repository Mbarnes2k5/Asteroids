import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        #Sub classes override
        pass

    def update(self, dt):
        #Sub classes override
        pass

    def collision(circleshape_a ,circleshape_b):
        distance = pygame.Vector2.distance_to(circleshape_b.position, circleshape_a.position)  
        radius = circleshape_a.radius + circleshape_b.radius
        if distance <= radius:
            return True
        else:
            return False
