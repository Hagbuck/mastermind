from model import Board
from ui import UIBoard
from basic_ai import basic_ai
from stats import Stats


import sys, pygame, csv

colors = {
    "black" : (0, 0, 0),
    "white" : (255, 255, 255),
    "dark_red" : (100, 0, 0),
}

if __name__ == '__main__':
    pygame.init()

    window_size = width, height = 1200, 600
    screen = pygame.display.set_mode(window_size)

    b = UIBoard()
    ai = basic_ai(b)
    stats = Stats(b)


    loop = True
    auto_mod = True
    ui = True

    while loop:
        if auto_mod:
            if b.is_win() or b.is_loose():
                stats.register_data(b)
                b.reset()
                ai.reset()
            else:
                # pygame.time.delay(100)
                ai.next_move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                elif event.key == pygame.K_a:
                    auto_mod = not auto_mod

                elif auto_mod == False:
                    if event.key == pygame.K_SPACE:
                        if b.is_win() or b.is_loose():
                            b.reset()
                            ai.reset()
                        else:
                            ai.next_move()
        if ui:
            if b.is_loose():
                for i in range(0, 3):
                    screen.fill(colors["dark_red"])
                    b.draw(screen, ai.moves)
                    pygame.display.flip()
                    pygame.time.delay(40)

                    screen.fill(colors["black"])
                    b.draw(screen, ai.moves)
                    pygame.display.flip()
                    pygame.time.delay(40)


            screen.fill(colors["black"])
            b.draw(screen, ai.moves)
            pygame.display.flip()

    stats.save_file()
    print(stats)