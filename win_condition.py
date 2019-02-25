class WinCondition():
    def __init__ (self, current_board, win_condition, current_move_row, current_move_column):
        self.win_condition = win_condition
        self.board = current_board
        self.current_move_row = current_move_row
        self.current_move_column = current_move_column
    
    def check_row(self):
        for x in range(self.win_condition):
            current_position = self.current_move_column - x

            #check if row is not out of bounds
            if current_position + self.win_condition <= len(self.board[0]) and current_position >= 0:
                #print([self.board[self.current_move_row][current_position + element] for element in range(self.win_condition)])
                row_eval = { self.board[self.current_move_row][current_position + element] for element in range(self.win_condition) }
                if len(row_eval) == 1 and 0 not in row_eval:
                    return True
        return False 
    
    def check_column(self):
        for y in range(self.win_condition):
            current_position = self.current_move_row - y

            #check if column is not out of bounds
            if current_position + self.win_condition <= len(self.board) and current_position >= 0:
                #print([self.board[current_position+element][self.current_move_column] for element in range(self.win_condition)])
                column_eval = {self.board[current_position+element][self.current_move_column] for element in range(self.win_condition) }
                if len(column_eval) == 1 and 0 not in column_eval:
                    return True

        return False
    
    def check_diag_one(self):
        for d_one in range(self.win_condition):
            current_element_x = self.current_move_row - d_one
            current_element_y = self.current_move_column - d_one
            #check if row is not out of bounds.
            if current_element_x + self.win_condition <= len(self.board) and current_element_x >= 0:
                #check if column is not out of bounds.
                if current_element_y + self.win_condition <= len(self.board[0]) and current_element_y >= 0:                
                    #print([self.board[current_element_x+element][current_element_y+element] for element in range(self.win_condition)])
                    d_one_eval = {self.board[current_element_x+element][current_element_y+element] for element in range(self.win_condition)}
                    if len(d_one_eval) == 1 and 0 not in d_one_eval:
                        return True
        return False 
    
    def check_diag_two(self):
        for d_two in range(self.win_condition):
            current_element_x = self.current_move_row + d_two
            current_element_y = self.current_move_column - d_two
            #check if row is not out of bounds
            if current_element_x < len(self.board) and current_element_x + 1 - self.win_condition >= 0:
                #check if column is not out of bounds.
                if current_element_y + self.win_condition <= len(self.board[0]) and current_element_y >= 0:   
                    #print([self.board[current_element_x-element][current_element_y+element] for element in range(self.win_condition)])
                    d_two_eval = {self.board[current_element_x-element][current_element_y+element] for element in range(self.win_condition)}
                    if len(d_two_eval) == 1 and 0 not in d_two_eval:
                        return True
        return False 

    def run(self):
        #print(self.board)
        if self.check_column() or self.check_row() or self.check_diag_one() or self.check_diag_two():
            return True
        return False
