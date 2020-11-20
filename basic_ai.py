import random

"""
Basic AI : Take a list that contains all the possible move and reduce it at each play
"""
def basic_ai(b):
    moves = b.all_moves()
    print("Possibles moves ({}) : {}".format(len(moves), moves))
    move = random.choice(moves)

    while(b.is_move_allowed(move)):
        b.play(move)
        moves.remove(move)
        print(b)

        if b.is_solution(move):
            print('WIN')
            break

        moves = b.reduce_moves(moves)
        print("Possibles moves ({}) : {}".format(len(moves), moves))
        move = random.choice(moves)