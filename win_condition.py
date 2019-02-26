class WinCondition:
    ''' Provides methods for checking  for customizable win conditions. '''

    def __init__(self, current_board, win_threshold, current_move_row, current_move_column):
        ''' Sets current board position, co-ordinates of current move and win_threshold (how many in a row does a player
            need to get in order to win)'''
        self.win_threshold = win_threshold
        self.board = current_board
        self.current_move_row = current_move_row
        self.current_move_column = current_move_column

    def check_row(self):
        '''Checks if a win condition is met in the row the current move was made'''
        for x in range(self.win_threshold):
            current_position = self.current_move_column - x
            # check if row is not out of bounds
            if current_position + self.win_threshold <= len(self.board[0]) and current_position >= 0:
                # DEBUG
                # print([self.board[self.current_move_row][current_position + element] for element in range(self.win_threshold)])
                row_eval = {self.board[self.current_move_row][current_position + element] for element in
                            range(self.win_threshold)}
                if len(row_eval) == 1 and 0 not in row_eval:
                    return True
        return False

    def check_column(self):
        '''Checks if a win condition is met in the column the current move was made'''
        for y in range(self.win_threshold):
            current_position = self.current_move_row - y

            # check if column is not out of bounds
            if current_position + self.win_threshold <= len(self.board) and current_position >= 0:
                # DEBUG
                # print([self.board[current_position+element][self.current_move_column] for element in range(self.win_threshold)])
                column_eval = {self.board[current_position + element][self.current_move_column] for element in
                               range(self.win_threshold)}
                if len(column_eval) == 1 and 0 not in column_eval:
                    return True

        return False

    def check_diag_one(self):
        '''Checks if a win condition is met in the descending diagonal the current move was made'''
        for d_one in range(self.win_threshold):
            current_element_x = self.current_move_row - d_one
            current_element_y = self.current_move_column - d_one
            # check if row/column is not out of bounds.
            if (current_element_x + self.win_threshold <= len(self.board) and current_element_x >= 0) and \
                    (current_element_y + self.win_threshold <= len(self.board[0]) and current_element_y >= 0):
                # DEBUG
                # print([self.board[current_element_x+element][current_element_y+element] for element in range(self.win_threshold)])
                d_one_eval = {self.board[current_element_x + element][current_element_y + element] for element in
                              range(self.win_threshold)}
                if len(d_one_eval) == 1 and 0 not in d_one_eval:
                    return True

        return False

    def check_diag_two(self):
        '''Checks if a win condition is met in the ascending diagonal the current move was made'''
        for d_two in range(self.win_threshold):
            current_element_x = self.current_move_row + d_two
            current_element_y = self.current_move_column - d_two
            # check if row/column is not out of bounds
            if (current_element_x < len(self.board) and current_element_x + 1 - self.win_threshold >= 0) and \
                    (current_element_y + self.win_threshold <= len(self.board[0]) and current_element_y >= 0):
                # DEBUG
                # print([self.board[current_element_x-element][current_element_y+element] for element in range(self.win_threshold)])
                d_two_eval = {self.board[current_element_x - element][current_element_y + element] for element in
                              range(self.win_threshold)}
                if len(d_two_eval) == 1 and 0 not in d_two_eval:
                    return True

        return False

    def evaluate(self):
        ''' Returns True if a win situation is present on the board.'''
        return self.check_column() or self.check_row() or self.check_diag_one() or self.check_diag_two()
