from win_condition import WinCondition
from game_io import GameInputOutput

class Board:
    def __init__(self, num_rows, num_columns):
        ''' Creates an empty board (filled with zeros) '''
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.board = [[0 for i in range(num_columns)] for j in range(num_rows)]
        

    def print_board(self):
        '''Prints the board'''
        GameInputOutput.print_board(self.board)


    def check_win(self, win_threshold):
        '''Checks if current move won the game.'''
        win = WinCondition(self.board, win_threshold,self.current_move[0], self.current_move[1])
        return(win.evaluate())
    
    def check_draw(self):
        '''Checks if the board is in a drawn position'''
        for row in range(len(self.board)):
            if 0 in self.board[row]:
                return False
        return True

    def process_move(self, column_num, player_num):
        ''' Processes the current move and sets the x,y of current move.

            if move column is full then the move is illegal and process returns false.
            if move is legal then process the move until the 'settles' according to game laws, process returns True.
        '''

        if self.board[0][column_num] != 0 or column_num > len(self.board[0]):
            return False

        for i in range(len(self.board)):
            if self.board[i][column_num] != 0 :
                self.board[i-1][column_num] = player_num
                self.current_move = [i, column_num]
                #print("move processed")
                return True
            elif i == len(self.board) - 1 and self.board[i][column_num] == 0:
                self.board[i][column_num] = player_num 
                self.current_move = [i, column_num]               
                return True
    


    