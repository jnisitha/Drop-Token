from win_threshold import WinCondition
import pytest

def test_integration():
    _board_one =[
                [0,1,0,1,2,5,4],
                [2,3,4,0,7,3,7],
                [3,1,4,0,3,3,1],
                [2,1,4,3,3,6,1],
                [1,2,3,3,6,7,3],
                [2,4,3,5,6,2,9]]

    _board_two = [
                [1, 0, 0, 0], 
                [1, 2, 0, 0], 
                [1, 2, 0, 0], 
                [1, 2, 0, 0]]

    _win_threshold = 4
    _current_move_row = 0
    _current_move_column = 0

    win = WinCondition(_board_two, _win_threshold, _current_move_row, _current_move_column)
    # print(win.check_row())
    # print(win.check_column())
    # print(win.check_diag_one())
    # print(win.check_diag_two())
    assert win.run() == True
