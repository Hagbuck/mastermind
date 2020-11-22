import random
import copy
import itertools

default_max_row = 10
default_row_size = 4
default_min_val = 1
default_max_val = 8

"""
Board of Mastermind
"""
class Board:
    """
    Create the board, if any solution is given, the solution is random
    """
    def __init__(self, max_row = default_max_row, row_size = default_row_size, min_val = default_min_val, max_val = default_max_val, solution = None):
        self.reset(max_row, row_size, min_val, max_val, solution)

    def reset(self, max_row = default_max_row, row_size = default_row_size, min_val = default_min_val, max_val = default_max_val, solution = None):
        self.i = -1
        self.rows = []
        self.res = []
        self.max_row = max_row
        self.row_size = row_size
        self.min_val = min_val
        self.max_val = max_val

        if max_row <= 0:
            raise ValueError("max_row({}) must be a positif integer".format(max_row))

        if row_size <= 0:
            raise ValueError("row_size({}) must be a positif integer".format(row_size))            

        if min_val > max_val:
            raise ValueError("min_val({}) is greater than max_val({})".format(min_val, max_val))

        if solution:
            self.solution = solution

            if len(self.solution) != self.row_size:
                raise ValueError("Solution array({}) doesn't have the same length as row_size({})".format(self.solution, row_size))

            elif min(self.solution) < self.min_val:
                raise ValueError("Solution array({}) contain a lower value than min_val({})".format(self.solution, self.min_val))

            elif max(self.solution) > self.max_val:
                raise ValueError("Solution array({}) contain a lower value than max_val({})".format(self.solution, self.max_val))
        else:
            self.solution = self.get_random_move() 

    """
    Return a copy of the board
    """
    def copy(self):
        return copy.deepcopy(self)

    """
    Return True if a move is allow, False otherwise
    """
    def is_move_allowed(self, r):
        # Board full
        if self.i >= self.max_row - 1:
            return False

        # Wrong size
        if not r or len(r) != self.row_size:
            return False

        # Check if values or allowed
        for v in r:
            if v > self.max_val or v < self.min_val:
                return False

        return True

    """
    Return True if the move (r) is the solution
    """
    def is_solution(self, r):
        # Wrong size
        if not r or len(r) != self.row_size:
            return False

        for i in range(0, len(r)):
            if r[i] != self.solution[i]:
                return False
        return True

    """
    Return True if the last move win the game, False otherwise
    """
    def is_win(self):
        if len(self.res) > 0:
            if self.res[-1]["good"] == self.row_size:
                return True
        return False

    """
    Return True if the last move loose the game, False otherwise
    """
    def is_loose(self):
        if len(self.res) == self.max_row and len(self.res) > 0:
            if self.res[-1]["good"] < self.row_size:
                return True
        return False


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
    def get_random_move(self):
        move = []
        for i in range(0, self.row_size):
            move.append(random.randint(self.min_val, self.max_val))
        return move
    
    """
    Generate all the possible moves
    """
    def all_moves(self):
        return list(itertools.product(list(range(self.min_val, self.max_val+1)), repeat = self.row_size))

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
        sep = '-' * ((2+self.row_size)*2-1) + '\n'
        s = ('---(' + str(self.i + 1) + '/' + str(self.max_row) + ')---\n')

        for i in range(0, len(self.rows)):
            s += '| '
            for j in range(0, len(self.rows[i])):
                s += str(self.rows[i][j]) + ' '
            s += '| {} {}\n'.format(self.res[i]["good"], self.res[i]["wrong"])

        for i in range(len(self.rows), self.max_row):
            s += '| ' + ('. ' * self.row_size) + '|\n'

        s += sep
        s += '| '
        for v in self.solution:
            s += '{} '.format(v)
        s += '|\n'
        s += sep
        return s