# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
    clock = pygame.time.Clock()
    dt = 0

    # Create empty named groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add classes to groups
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    # Create objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    # Game Starts
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # .update on each object that is in the updatable group (by class)
        for obj in updatable:
            obj.update(dt)

        # .draw on each object that is in the drawable group (by class)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        clock.tick(60)                  #Sets draw speed to 60fps
        dt = clock.get_time() / 1000   #Records increments delta time stored value

if __name__ == "__main__":
    main()
