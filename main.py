import pygame
from constants import *

def main():
    pygame.init()
    
    py_clock = pygame.time.Clock()
    
    dt = 0
    frame_rate = 60

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        fps_counter(screen, py_clock)
        pygame.display.flip()
        
        dt = (py_clock.tick(frame_rate))/1000 #Binding game to FPS
        

def fps_counter(display_screen, game_clock):
    fps_font =  pygame.font.Font(None, 36)
    
    fps = str(int(game_clock.get_fps()))
    fps_t = fps_font.render(fps , 1, pygame.Color("RED"))
    display_screen.blit(fps_t,(0,0))


if __name__ == "__main__":
    main()
