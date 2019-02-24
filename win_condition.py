_board_one =[[0,1,0,1,2,5],
            [2,3,4,2,7,6],
            [3,1,4,0,5,3],
            [2,1,4,3,5,6],
            [1,2,5,3,6,7],
            [2,4,3,5,6,2]]

_win_condition = 3
_current_move_row = 3
_current_move_column = 3

class WinCondition():
    def __init__ (self, current_board, win_condition, current_move_row, current_move_column):
        self.win_condition = win_condition
        self.board = current_board
        self.current_move_row = current_move_row
        self.current_move_column = current_move_column
    
    def check_row(self):
        for x in range(self.win_condition):
            current_position = self.current_move_column - x
            print(self.board[self.current_move_row][current_position:current_position+self.win_condition])
            row_eval = set( self.board[self.current_move_row][current_position:current_position+self.win_condition] )
            if len(row_eval) == 1 and 0 not in row_eval:
                return True
        return False 
    
    def check_column(self):
        for y in range(self.win_condition):
            current_position = self.current_move_row - y
            print([self.board[current_position+element][self.current_move_column] for element in range(self.win_condition)  ])
            column_eval = {self.board[current_position+element][self.current_move_column] for element in range(self.win_condition) }
            if len(column_eval) == 1 and 0 not in column_eval:
                return True

        return False
    
    def check_diag_one(self):
        for d_one in range(self.win_condition):
            current_element_x = self.current_move_row - d_one
            current_element_y = self.current_move_column - d_one
            d_one_eval = {self.board[current_element_x+element][current_element_y+element] for element in range(self.win_condition)}
            if len(d_one_eval) == 1 and 0 not in d_one_eval:
                return True
        return False 
    
    def check_diag_two(self):
        for d_two in range(self.win_condition):
            current_element_x = self.current_move_row + d_two
            current_element_y = self.current_move_column - d_two
            d_two_eval = {self.board[current_element_x-element][current_element_y+element] for element in range(self.win_condition)}
            if len(d_two_eval) == 1 and 0 not in d_two_eval:
                return True
        return False 

    def run(self):
        if self.check_column() or self.check_row() or self.check_diag_one() or self.check_diag_two():
            return True
        return False

win = WinCondition(_board_one, _win_condition, _current_move_row, _current_move_column)
print(win.check_column())
print(win.check_row())