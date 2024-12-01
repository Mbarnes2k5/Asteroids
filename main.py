import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot 

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group() 

    Player.containers = (updatable, drawable,)
    Asteroid.containers = (asteroids, updatable, drawable, ) 
    AsteroidField.containers = (updatable,)
    Shot.containers = ( shot,updatable,drawable) 

    pygame.init()
    font = pygame.font.Font(None, 36)
    pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    dt = 0
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()    
    while True:
        #     print(f"Number of sprites in updatable group: {len(updatable)}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        screen.fill('Black')
        for aster in asteroids: 
            for sht in shot: 
                if sht.collision(aster): 
                    player.scoring(aster)
                    aster.split() 
                    sht.kill()

        for sprite in updatable:
            sprite.update(dt) 

        for sprite in asteroids: 
            if sprite.collision(player) == True :
                if not player.is_invincible():
                   player.take_hit() 
            else :
                continue

        for sprite in drawable:
            sprite.draw(screen)
        
        score_text = font.render(f'Score: {player.score}', True, 'red')
        score_x = SCREEN_WIDTH - score_text.get_width() - 10
        shield_text = font.render(f'Shields: {player.shields}',True ,'cyan')
        screen.blit(shield_text, (10,10))
        screen.blit(score_text, (score_x,10))
        pygame.display.flip()
if __name__ == "__main__":
   main()
