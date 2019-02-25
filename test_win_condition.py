from win_condition import WinCondition
import pytest

def test_integration():
    board_one =[
                [0,1,0,1,2,5,4],
                [2,3,4,0,7,3,7],
                [3,1,4,0,3,3,1],
                [2,1,4,3,3,6,1],
                [1,2,3,3,6,7,3],
                [2,4,3,5,6,2,9]]

    board_two = [
                [1, 0, 0, 0], 
                [1, 2, 0, 0], 
                [1, 2, 0, 0], 
                [1, 2, 0, 0]]

    win = WinCondition(board_two, 4, 0, 0)
    # win = WinCondition(board_two, win_threshold, current_move_row, current_move_column)


    assert win.evaluate() == True


def test_check_row():
    row_1 = [[0,0,2,3,3,3,4,4,4,4,4,5,6]]
    row_2 = [[0,0,0,0,0,0,0,0,0,0,0,0]]
    row_3 = [[1,0,0,0,0,0,1,1,1]]

    win_1 = WinCondition(row_1, 3, 0, 3)
    win_2 = WinCondition(row_2, 3, 0, 3)
    win_3 = WinCondition(row_3, 3, 0, 8)
    win_4 = WinCondition(row_3, 4, 0, 3)
    win_5 = WinCondition(row_1, 5, 0, 6)

    assert win_1.check_row() == True
    assert win_2.check_row() == False
    assert win_3.check_row() == True
    assert win_4.check_row() == False
    assert win_5.check_row() == True


def test_check_column():
    column_1 = [[0], [1], [1], [1], [2], [3], [1]]
    column_2 = [[1], [2], [3], [3], [1], [3], [1], [1]]
    column_3 = [[5], [6], [5], [5], [5], [5], [5], [5]]

    win_1 = WinCondition(column_1, 3, 1, 0)
    win_2 = WinCondition(column_2, 3, 4, 0)
    win_3 = WinCondition(column_3, 6, 7, 0)
    win_4 = WinCondition(column_3, 4, 3, 0)
    win_5 = WinCondition(column_2, 3, 7, 0)

    assert win_1.check_column() == True
    assert win_2.check_column() == False
    assert win_3.check_column() == True
    assert win_4.check_column() == True
    assert win_5.check_column() == False

