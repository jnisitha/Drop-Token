from win_condition import WinCondition
import pytest


board_one = [[1, 0, 0, 2], 
             [1, 2, 0, 2], 
             [1, 2, 0, 2], 
             [1, 1, 1, 1]]

#            0 1 2 3 4 5 6
board_two =[[0,1,0,1,2,5,4],# 0
            [2,3,4,0,7,3,7],# 1
            [3,1,4,0,3,3,1],# 2
            [2,1,4,3,3,6,1],# 3
            [1,2,3,3,6,7,3],# 4
            [2,4,3,5,6,2,1],# 5
            [0,0,2,3,3,3,1],# 6
            [0,4,4,4,4,4,1],# 7
            [2,3,4,0,7,3,1],# 8
            [1,2,3,3,6,7,1]]# 9


def test_check_column():

    win_1 = WinCondition(board_one[0], 3, 3, 0)
    win_2 = WinCondition(board_one[3], 3, 0, 3)
    win_3 = WinCondition(board_two[2], 3, 1, 2)
    win_4 = WinCondition(board_two[2], 3, 3, 2)
    win_5 = WinCondition(board_two[6], 5, 7, 6)

    assert win_1.check_column() == True
    assert win_2.check_column() == True
    assert win_3.check_column() == True
    assert win_4.check_column() == True
    assert win_5.check_column() == True


def test_check_row():

    win_1 = WinCondition(board_one[2], 4, 0, 0)
    win_2 = WinCondition(board_one[3], 4, 3, 3)
    win_3 = WinCondition(board_two[7], 5, 7, 5)
    win_4 = WinCondition(board_two[5], 4, 5, 3)
    win_5 = WinCondition(board_two[6], 3, 6, 3)

    assert win_1.check_row() == False
    assert win_2.check_row() == True
    assert win_3.check_row() == True
    assert win_4.check_row() == False
    assert win_5.check_row() == True





def test_integration():
    

    win = WinCondition(board_two, 4, 0, 0)
    # win = WinCondition(board_two, win_threshold, current_move_row, current_move_column)


    assert win.evaluate() == True
