import random
from model import Board

"""
Basic AI : Take a list that contains all the possible move and reduce it at each play
"""
class basic_ai:
    def __init__(self, board):
        self.board = board
        self.moves = []
        self.reset()

        #print("Possibles moves ({}) : {}".format(len(moves), moves))

    def reset(self):
        self.moves = self.board.all_moves()


    def next_move(self):
        if self.board.is_win() == False and self.board.is_loose() == False:
            move = random.choice(self.moves)
            # move = self.moves[0]

            if self.board.is_move_allowed(move):
                self.board.play(move)
                self.moves.remove(move)

                self.moves = self.board.reduce_moves(self.moves)
                #print("Possibles moves ({}) : {}".format(len(moves), moves))