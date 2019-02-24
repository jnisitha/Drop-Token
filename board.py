from win_condition import WinCondition

class Board:
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self._board = [[0 for i in range(num_rows)] for j in range(num_columns)]
        

    def print_board(self):
        for i in range(len(self._board)):
            print("| " + ' '.join([str(v) for v in self._board[i]]))
        
        print("+" + "-" * len(self._board[0]) * 2)
        print("  " + ' '.join([str(i) for i in range(1, 1 + len(self._board[0]))]))

        return 0

    def check_win(self, win_condition):
        win = WinCondition(self._board, win_condition,self._current_move[0], self._current_move[1])
        print(win.run())
        return(win.run())

    def process_move(self, column_num, player_num):
        print("process move")

        if self._board[0][column_num] != 0:
            return False

        for i in range(len(self._board)):
            if self._board[i][column_num] != 0 :
                self._board[i-1][column_num] = player_num
                self._current_move = [i, column_num]
                print("move processed")
                return True
            elif i == len(self._board) - 1 and self._board[i][column_num] == 0:
                self._board[i][column_num] = player_num 
                self._current_move = [i, column_num]               
                return True
        
        
            
                   

        return 0
    
    def isLegal():
        return 0
    


    