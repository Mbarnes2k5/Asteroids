from circleshape import * 
from constants import * 
from shot import Shot 
import sys


class Player(CircleShape):
    containers = None
    def __init__(self,x,y): 
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x 
        self.last_hit_time = 0 #Start at 0 to allow the first hit
        self.last_shot_time = 0 
        self.y = y
        self.rotation = 0
        self.shields = 3
        self.score = 0 

        if Player.containers is not None:
            for container in Player.containers:
                container.add(self)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]: 
            self.move(dt)
        if keys[pygame.K_s]: 
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def is_invincible(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.last_hit_time < INVINCIBILITY_DURATION

    def take_hit(self):
        self.last_hit_time = pygame.time.get_ticks()
        self.shields -= 1
        if self.shields == 0 :
            print("Game over")
            sys.exit()
        
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(),2) 


    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED *dt 
    
    def shoot(self, dt):
        current_time = pygame.time.get_ticks()
        if self.last_shot_time == 0 or current_time - self.last_shot_time > PLAYER_SHOT_COOLDOWN:
            shot_velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            print(f"Rotation: {self.rotation}, Shot Velocity: {shot_velocity}")
            new_shot = Shot(self.position.x, self.position.y, shot_velocity) 
            self.last_shot_time = current_time
   
    def scoring(self, astro_size):
            if astro_size.radius <= ASTEROID_MAX_RADIUS and astro_size.radius >= 50:
                self.score += 100 
            elif astro_size.radius <= 49 and astro_size.radius >= 30:
                self.score += 300 
            elif astro_size.radius <= 29 and astro_size.radius >= 20:
                self.score += 500 
            return 

