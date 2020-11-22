from mastermind.model import Board
#####################################################
# Board.reset() and also __init__()
#####################################################

# Check min_val > max_val
# row_size != solution
# solution min < min_val
# solution max > mmax_val
# max_row <= 0


#####################################################
# Board.copy()
#####################################################

def test_board_copy_is_a_real_copy():
    b = Board()
    bc = b.copy()
    assert b != bc


#####################################################
# Board.is_move_allowed()
#####################################################

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
    m[0] = b.min_val - 1
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_none_move():
    b = Board(max_row = 1)
    m = None
    assert b.is_move_allowed(m) == False


#####################################################
# Board.is_solution()
#####################################################

def test_board_is_solution_good_solution():
    b = Board(row_size = 3, min_val = 1, solution = [1, 1, 1])
    m =  [1, 1, 1]
    assert b.is_solution(m) == True

def test_board_is_solution_wrong_solution():
    b = Board(row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m =  [1, 2, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_move_too_big():
    b = Board(row_size = 3, min_val = 1, solution = [1, 1, 1])
    m = [1, 1, 1, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_move_too_short():
    b = Board(row_size = 3, min_val = 1, solution = [1, 1, 1])
    m = [1, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_none_solution():
    b = Board(row_size = 3, min_val = 1, solution = [1, 1, 1])
    m = None
    assert b.is_solution(m) == False

    
#####################################################
# Board.is_win()
#####################################################


#####################################################
# Board.is_loose()
#####################################################


#####################################################
# Board.evaluate()
#####################################################


#####################################################
# Board.play()
#####################################################


#####################################################
# Board.get_random_move()
#####################################################


#####################################################
# Board.all_move()
#####################################################


#####################################################
# Board.reduce_moves()
#####################################################

