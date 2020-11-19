import random

def basic_ai(b):
    moves = b.all_moves()
    print(moves)
    move = random.choice(moves)

    while(b.is_move_allowed(move)):
        b.play(move)
        moves.remove(move)
        print(b)

        if b.is_solution(move):
            print('WIN')
            exit()

        moves = b.reduce_moves(moves)
        print(moves)
        move = random.choice(moves)
        