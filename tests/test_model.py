from mastermind.model import Board

# Board.copy()
def test_board_copy_is_a_real_copy():
    b = Board()
    bc = b.copy()
    assert b != bc

# Board.is_move_allowed()
def test_board_is_move_allowed_board_full():
    b = Board(max_row = 1)
    m = b.get_random_move()
    b.play(m)
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_to_big():
    b = Board(max_row = 1)
    m = b.get_random_move()
    m.append(b.min_val)
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_to_short():
    b = Board(max_row = 1)
    m = b.get_random_move()
    m.pop()
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_contain_higher_value():
    b = Board(max_row = 1)
    m = b.get_random_move()
    m[0] = b.max_val + 1
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_contain_lower_value():
    b = Board(max_row = 1)
    m = b.get_random_move()
    m[0] = b.min_val -1
    assert b.is_move_allowed(m) == False

# Board.is_solution()

# Board.is_win()

# Board.is_loose()

# Board.evaluate()

# Board.play()

# Board.get_random_move()

# Board.all_move()

# Board.reduce_moves()
