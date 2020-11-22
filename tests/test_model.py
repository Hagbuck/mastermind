import pytest

from mastermind.model import Board

#####################################################
# Board.reset() and also __init__()
#####################################################

def test_board_reset_min_val_gt_max_val():
    with pytest.raises(ValueError):
        b = Board(min_val = 3, max_val = 1)

def test_board_reset_solution_bad_size():
    with pytest.raises(ValueError):
        b = Board(max_row = 1, row_size = 3, solution = [1, 1, 1, 1])

def test_board_reset_solution_contain_lower_value_than_min_val():
    with pytest.raises(ValueError):
        b = Board(max_row = 1, row_size = 3, min_val = 1, max_val = 2, solution = [0, 1, 1])

def test_board_reset_solution_contain_highter_value_than_max_val():
    with pytest.raises(ValueError):
        b = Board(max_row = 1, row_size = 3, min_val = 1, max_val = 2, solution = [3, 1, 1])

def test_board_reset_max_row_positif():
    b = Board(max_row = 1)
    # Should raise no Exception

def test_board_reset_max_row_equals_zero():
    with pytest.raises(ValueError):
        b = Board(max_row = 0)

def test_board_reset_max_row_negatif():
    with pytest.raises(ValueError):
        b = Board(max_row = -1)

def test_board_reset_row_size_positif():
    b = Board(row_size = 1)
    # Should raise no Exception

def test_board_reset_row_size_equals_zero():
    with pytest.raises(ValueError):
        b = Board(row_size = 0)

def test_board_reset_row_size_negatif():
    with pytest.raises(ValueError):
        b = Board(row_size = -1)


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

def test_board_is_move_allowed_board_full():
    b = Board(max_row = 2, row_size = 4, min_val = 1, solution = [1, 1, 1, 1])
    m = [1, 1, 1, 1]
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
    b = Board(max_row = 1, max_val = 3)
    m = b.get_random_move()
    m[0] = b.max_val + 1
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_contain_lower_value():
    b = Board(max_row = 1, min_val = 1)
    m = b.get_random_move()
    m[0] = b.min_val - 1
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_none_move():
    b = Board(max_row = 1)
    m = None
    assert b.is_move_allowed(m) == False

def test_board_is_move_allowed_move_contain_None_value():
    b = Board(max_row = 1, row_size = 3)
    m = [None, 1, 1]
    assert b.is_move_allowed(m) == False


#####################################################
# Board.is_solution()
#####################################################

def test_board_is_solution_good_solution():
    b = Board(row_size = 3, max_row = 1, min_val = 1, solution = [1, 1, 1])
    m =  [1, 1, 1]
    assert b.is_solution(m) == True

def test_board_is_solution_wrong_solution():
    b = Board(row_size = 3, max_row = 1, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m =  [1, 2, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_move_too_big():
    b = Board(row_size = 3, max_row = 1, min_val = 1, solution = [1, 1, 1])
    m = [1, 1, 1, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_move_too_short():
    b = Board(row_size = 3, max_row = 1, min_val = 1, solution = [1, 1, 1])
    m = [1, 1]
    assert b.is_solution(m) == False

def test_board_is_solution_none_solution():
    b = Board(row_size = 3, max_row = 1, min_val = 1, solution = [1, 1, 1])
    m = None
    assert b.is_solution(m) == False


#####################################################
# Board.is_win()
#####################################################

def test_board_is_win_last_move_win():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    m = [1, 1, 1]
    b.play(m)
    assert b.is_win() == True

def test_board_is_win_last_move_is_bad():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    m = [1, 1, 2]
    b.play(m)
    assert b.is_win() == False

def test_board_is_win_any_move():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    assert b.is_win() == False


#####################################################
# Board.is_loose()
#####################################################

def test_board_is_loose_last_move_win():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    m = [1, 1, 1]
    b.play(m)
    assert b.is_loose() == False

def test_board_is_loose_last_move_is_bad():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    m = [1, 1, 2]
    b.play(m)
    assert b.is_loose() == False

def test_board_is_loose_last_move_fill_the_board():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    m = [1, 1, 2]
    b.play(m)
    b.play(m)
    assert b.is_loose() == True

def test_board_is_loose_any_move():
    b = Board(row_size = 3, max_row = 2, solution = [1, 1, 1])
    assert b.is_loose() == False

#####################################################
# Board.evaluate()
#####################################################

def test_board_evaluate_all_good():
    rs = 3
    b = Board(max_row = 4, row_size = rs, min_val = 1, max_val = 3, solution = [1, 2, 2])
    m = [1, 2, 2]
    r = b.evaluate(m)
    assert r["good"] == rs and r["wrong"] == 0

def test_board_evaluate_nothing():
    b = Board(max_row = 4, row_size = 3, min_val = 1, max_val = 3, solution = [1, 2, 2])
    m = [3, 3, 3]
    r = b.evaluate(m)
    assert r["good"] == 0 and r["wrong"] == 0

def test_board_evaluate_all_wrong():
    rs = 3
    b = Board(max_row = 4, row_size = rs, min_val = 1, max_val = 3, solution = [1, 2, 3])
    m = [3, 1, 2]
    r = b.evaluate(m)
    assert r["good"] == 0 and r["wrong"] == rs

def test_board_evaluate_112_122_not_double_count_the_1_solution():
    b = Board(max_row = 4, row_size = 3, min_val = 1, max_val = 3, solution = [1, 2, 2])
    m = [1, 1, 2]
    r = b.evaluate(m)
    print(r)
    assert r["good"] == 2 and r["wrong"] == 0

def test_board_evaluate_122_112_count_the_1_move_for_only_one_1():
    b = Board(max_row = 4, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 2])
    m = [1, 2, 2]
    r = b.evaluate(m)
    print(r)
    assert r["good"] == 2 and r["wrong"] == 0

def test_board_evaluate_move_with_None():
    with pytest.raises(ValueError):
        b = Board(max_row = 4, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 2])
        m = [None, 2, 2]
        r = b.evaluate(m)
        print(r)

#####################################################
# Board.play()
#####################################################

def test_board_play_allowed_move():
    b = Board(max_row = 3, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m = [1, 2, 3]
    played = b.play(m)
    assert len(b.res) == 1 and len(b.rows) == 1 and played == True

def test_board_play_forbidden_move():
    b = Board(max_row = 3, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m = [1, 2, 5]
    played = b.play(m)
    assert len(b.res) == 0 and len(b.rows) == 0 and played == False

def test_board_play_board_full():
    b = Board(max_row = 1, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m = [1, 2, 3]
    b.play(m)
    played = b.play(m)
    assert len(b.res) == 1 and len(b.rows) == 1 and played == False

def test_board_play_after_win():
    b = Board(max_row = 2, row_size = 3, min_val = 1, max_val = 3, solution = [1, 1, 1])
    m = [1, 1, 1]
    b.play(m)
    played = b.play(m)
    assert len(b.res) == 1 and len(b.rows) == 1 and played == False

#####################################################
# Board.get_random_move()
#####################################################

def test_board_get_random_move_check_size():
    b = Board(row_size = 4)
    m = b.get_random_move()
    assert len(m) == b.row_size

#####################################################
# Board.all_moves()
#####################################################


#####################################################
# Board.reduce_moves()
#####################################################

