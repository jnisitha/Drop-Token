from board import Board
import pytest

board_one = [[1, 0, 2, 2], 
             [1, 1, 2, 2], 
             [1, 2, 1, 2], 
             [1, 1, 1, 1]]

board_two = [[1, 2, 2, 2], 
             [1, 1, 2, 2], 
             [1, 2, 1, 2], 
             [1, 1, 1, 1]]

#              0 1 2 3 4 5 6
board_three =[[0,1,0,1,2,5,4],# 0
              [2,3,4,0,7,3,7],# 1
              [3,1,4,0,3,3,1],# 2
              [2,1,4,3,3,6,1],# 3
              [1,2,3,3,6,7,3],# 4
              [2,4,3,5,6,2,1],# 5
              [0,0,2,3,3,3,1],# 6
              [3,4,4,4,4,4,1],# 7
              [2,3,4,0,7,3,1],# 8
              [1,2,3,3,6,7,1]]# 9

def test_check_draw():
    board_1 = Board(4,4)
    board_1.board = board_one

    board_2 = Board(4,4)
    board_2.board = board_two

    assert board_1.check_draw() == False
    assert board_2.check_draw() == True

def test_process_move():
    board_1 = Board(4,4)
    board_1.board = board_one

    board_2 = Board(4,4)
    board_2.board = board_two

    assert board_1.process_move(1,2) == True
    assert board_1.process_move(3,2) == False