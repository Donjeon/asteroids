import pygame
from constants import *
from circleshape import * 
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    py_clock = pygame.time.Clock()
    
    dt = 0
    frame_rate = 60

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player_ship = Player(player_x, player_y)

    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player_ship.update(dt)

        for item in updatable:
            item.update(dt)

            


        screen.fill("black")
        fps_counter(screen, py_clock)

        #Player functions
        
        #player_ship.draw(screen)
        
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.is_colliding(player_ship):
                print("Game over!")
                exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        dt = (py_clock.tick(frame_rate))/1000 #Binding game to FPS

    
        

def fps_counter(display_screen, game_clock):
    fps_font =  pygame.font.Font(None, 36)
    
    fps = str(int(game_clock.get_fps()))
    fps_t = fps_font.render(fps , 1, pygame.Color("RED"))
    display_screen.blit(fps_t,(0,0))


if __name__ == "__main__":
    main()

