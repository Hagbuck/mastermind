import random
import copy
import itertools

max_row = 10
row_size = 4
min_val = 1
max_val = 8

"""
Board of Mastermind
"""
class Board:
    """
    Create the board, if any solution is given, the solution is random
    """
    def __init__(self, solution = None):
        self.solution = self.random_move() if solution == None else solution
        self.i = -1
        self.rows = []
        self.res = []

    """
    Return a copy of the board
    """
    def copy(self):
        return copy.deepcopy(self)

    """
    Return True if a move is allow, False otherwise
    """
    def is_move_allowed(self, r):
        if self.i >= max_row - 1:
            return False

        if len(r) != row_size:
            return False

        for v in r:
            if v > max_val or v < min_val:
                return False

        return True

    """
    Return True if the move (r) is the solution
    """
    def is_solution(self, r):
        for i in range(0, len(r)):
            if r[i] != self.solution[i]:
                return False
        return True

    """
    Evaluate a move and save the result into self.res
    It should be call only by the play method
    """
    def evaluate(self, move):
        res = {}
        res['good'] = 0
        res['wrong'] = 0
        s = list(self.solution)
        r = list(move)

        for i in range(0, len(r)):
            if s[i] == r[i]:
                res["good"] += 1
                s[i] = None
                r[i] = None

        for i in range(0, len(r)):
            if r[i] != None and r[i] in s:
                res['wrong'] += 1
                s[s.index(r[i])] = None
                r[i] = None 
        self.res.append(res)

    """
    Play a move(r)
    """
    def play(self, r):
        can_play = self.is_move_allowed(r)
        if can_play:
            self.rows.append(r)
            self.i += 1
            self.evaluate(r)

    """
    Generate a random move
    """
    def random_move(self):
        move = []
        for i in range(0, row_size):
            move.append(random.randint(min_val, max_val))
        return move
    
    """
    Generate all the possible moves
    """
    def all_moves(self):
        return list(itertools.product(list(range(min_val, max_val+1)),repeat = row_size))

    """
    Get all moves with taking in consideration the last move
    """
    def reduce_moves(self, moves):
        last_res = self.res[self.i]

        ms = list(moves)
        new_moves = []

        # For each possible move
        for move in ms:
            m = list(move)
            last_m = list(self.rows[self.i])
            good_found = 0

            # Browse each pawn
            for i in range(0, len(m)):

                # Count the good placed
                if m[i] == last_m[i]:
                    good_found += 1
                    m[i] = None
                    last_m[i] = None

            # We need to have the same number of good
            if good_found == last_res["good"]:
                wrong_founded = 0

                for i in range(0, len(m)):

                    # Count the wrong placed
                    if m[i] != None and m[i] in last_m:
                        wrong_founded += 1
                        last_m[last_m.index(m[i])] = None
                        m[i] = None

                if wrong_founded == last_res["wrong"]:
                    new_moves.append(move)


        return list(new_moves)

    """
    Return a string that contain the board
    """
    def __str__(self):
        sep = '-' * ((2+row_size)*2-1) + '\n'
        s = ('---(' + str(self.i + 1) + '/' + str(max_row) + ')---\n')

        for i in range(0, len(self.rows)):
            s += '| '
            for j in range(0, len(self.rows[i])):
                s += str(self.rows[i][j]) + ' '
            s += '| {} {}\n'.format(self.res[i]["good"], self.res[i]["wrong"])

        for i in range(len(self.rows), max_row):
            s += '| ' + ('. ' * row_size) + '|\n'

        s += sep
        s += '| '
        for v in self.solution:
            s += '{} '.format(v)
        s += '|\n'
        s += sep
        return s