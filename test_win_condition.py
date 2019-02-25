from win_condition import WinCondition
import pytest


board_one = [[1, 0, 2, 2], 
             [1, 1, 2, 2], 
             [1, 2, 1, 2], 
             [1, 1, 1, 1]]

#            0 1 2 3 4 5 6
board_two =[[0,1,0,1,2,5,4],# 0
            [2,3,4,0,7,3,7],# 1
            [3,1,4,0,3,3,1],# 2
            [2,1,4,3,3,6,1],# 3
            [1,2,3,3,6,7,3],# 4
            [2,4,3,5,6,2,1],# 5
            [0,0,2,3,3,3,1],# 6
            [3,4,4,4,4,4,1],# 7
            [2,3,4,0,7,3,1],# 8
            [1,2,3,3,6,7,1]]# 9

def test_evaluate():
    win_1 = WinCondition(board_one, 4, 0, 3)
    win_2 = WinCondition(board_one, 4, 2, 0)
    win_3 = WinCondition(board_two, 4, 1, 5)
    win_4 = WinCondition(board_two, 3, 7, 0)
    win_5 = WinCondition(board_two, 5, 9, 6)
    win_6 = WinCondition(board_one, 4, 0, 0)

    assert win_1.evaluate() == False
    assert win_2.evaluate() == True
    assert win_3.evaluate() == True
    assert win_4.evaluate() == True
    assert win_5.evaluate() == True
    assert win_6.evaluate() == True

def test_diag_two():
    win_1 = WinCondition(board_one, 4, 0, 3)
    win_2 = WinCondition(board_one, 3, 1, 2)
    win_3 = WinCondition(board_two, 4, 1, 5)
    win_4 = WinCondition(board_two, 3, 9, 6)
    win_5 = WinCondition(board_two, 3, 8, 1)

    assert win_1.check_diag_two() == False
    assert win_2.check_diag_two() == True
    assert win_3.check_diag_two() == True
    assert win_4.check_diag_two() == False
    assert win_5.check_diag_two() == False

def test_diag_one():
    win_1 = WinCondition(board_one, 4, 1, 1)
    win_2 = WinCondition(board_one, 4, 2, 1)
    win_3 = WinCondition(board_two, 4, 1, 5)
    win_4 = WinCondition(board_two, 3, 9, 6)
    win_5 = WinCondition(board_two, 3, 8, 1)

    assert win_1.check_diag_one() == True
    assert win_2.check_diag_one() == False
    assert win_3.check_diag_one() == False
    assert win_4.check_diag_one() == False
    assert win_5.check_diag_one() == True


def test_check_column():

    win_1 = WinCondition(board_one, 4, 3, 0)
    win_2 = WinCondition(board_one, 4, 0, 3)
    win_3 = WinCondition(board_two, 3, 1, 2)
    win_4 = WinCondition(board_two, 3, 3, 2)
    win_5 = WinCondition(board_two, 5, 7, 6)

    assert win_1.check_column() == True
    assert win_2.check_column() == False
    assert win_3.check_column() == True
    assert win_4.check_column() == True
    assert win_5.check_column() == True


def test_check_row():

    win_1 = WinCondition(board_one, 4, 0, 0)
    win_2 = WinCondition(board_one, 4, 3, 3)
    win_3 = WinCondition(board_two, 5, 7, 5)
    win_4 = WinCondition(board_two, 4, 5, 3)
    win_5 = WinCondition(board_two, 3, 6, 3)

    assert win_1.check_row() == False
    assert win_2.check_row() == True
    assert win_3.check_row() == True
    assert win_4.check_row() == False
    assert win_5.check_row() == True
