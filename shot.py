import pygame
from circleshape import CircleShape
from constants import * 

class Shot(CircleShape): 
    containers = () 
    def __init__(self, x,y, shot_velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.radius = SHOT_RADIUS 
        self.shot_velocity = shot_velocity
        self.velocity = pygame.Vector2(0,0)
        self.rotation = 0
        if Shot.containers is not None: 
            for container in Shot.containers:
                container.add(self) 
    

    def draw(self, screen): 
    
        

        glow_buffer = 100 
        size_x = size_y = 2 * (self.radius + glow_buffer) 
        glow_surface = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
        glow_surface.fill((0,0,0,0))
        
        center = (size_x // 2, size_y //2) 

        #Draw Circlee
        pygame.draw.circle(screen, (255,0,0), (self.position.x,self.position.y), self.radius, 0) 
        #Draw Glowing Circle
        pygame.draw.circle(glow_surface, (255,0,0,50),  center,self.radius + 3) 
        pygame.draw.circle(glow_surface, (255,0,0,30),  center,self.radius + 6) 
        pygame.draw.circle(glow_surface, (255,0,0,10),  center,self.radius + 9) 

        screen.blit(glow_surface, (self.position.x - size_x // 2, self.position.y - size_y //2), special_flags = pygame.BLEND_ADD)


    def update(self, dt): 
        self.position += self.shot_velocity * dt
    

