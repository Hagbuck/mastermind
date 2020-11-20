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
    ai = basic_ai(b)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    ai.next_move()

        screen.fill(black)
        b.draw(screen, True)
        pygame.display.flip()