import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable =  pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)

    
    player = Player(x = SCREEN_WIDTH/2 , y = SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    dt = 0
    while  True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        updatable.update(dt)

        for asteroid in asteroids:
            if(player.detect_collision(asteroid)):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.detect_collision(asteroid):
                    shot.kill()
                    asteroid.split()
        
        
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta/1000



if __name__ == "__main__":
    main()
