import random
from model import Board

"""
Basic AI : Take a list that contains all the possible move and reduce it at each play
"""
class basic_ai:
    def __init__(self, board):
        self.board = board
        self.moves = self.board.all_moves()

        #print("Possibles moves ({}) : {}".format(len(moves), moves))


    def next_move(self):
        if self.board.is_winned() == False:
            move = random.choice(self.moves)

            if self.board.is_move_allowed(move):
                self.board.play(move)
                self.moves.remove(move)

                self.moves = self.board.reduce_moves(self.moves)
                #print("Possibles moves ({}) : {}".format(len(moves), moves))