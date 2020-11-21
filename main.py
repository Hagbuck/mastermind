from model import Board
from ui import UIBoard
from basic_ai import basic_ai
from stats import Stats


import sys, pygame, time

colors = {
    "black" : (0, 0, 0),
    "white" : (255, 255, 255),
    "dark_red" : (100, 0, 0),
}

def auto_runner(b, ai, stats, occ):
    print('Running for {} iterations'.format(occ))
    beg = time.time()
    i = 0
    while i < occ:
        if b.is_win() or b.is_loose():
            stats.register_data(b)
            b.reset()
            ai.reset()
            i += 1
        else:
            ai.next_move()
    print('Finish in : {}'.format(time.time() - beg))

    stats.save_file()
    print(stats)

def pygame_run(b, ai, stats):
    pygame.init()

    window_size = width, height = 1200, 600
    screen = pygame.display.set_mode(window_size)

    loop = True
    auto_mod = True

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

if __name__ == '__main__':
    b = UIBoard()
    ai = basic_ai(b)

    if len(sys.argv) <= 1:
        stats = Stats(b)
        pygame_run(b, ai, stats)
    else:
        occ = int(sys.argv[1])
        stats = Stats(b, "{}_games.xlsx".format(occ))
        auto_runner(b, ai, stats, occ)
