from model import Board
from ui import UIBoard
from basic_ai import basic_ai

import sys, pygame

if __name__ == '__main__':
    pygame.init()

    window_size = width, height = 800, 600
    black = 0, 0, 0
    screen = pygame.display.set_mode(window_size)

    b = UIBoard()
    basic_ai(b)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

        screen.fill(black)
        #pygame.draw.ellipse(screen, (255,0,0), (0,0,64,64))
        b.draw(screen)
        pygame.display.flip()