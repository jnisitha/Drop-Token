

class Board:
    def __init__(self, num_rows, num_columns):
        self._board = [[0 for i in range(num_rows)] for j in range(num_columns)]
        

    def print_board(self):
        for i in range(len(self._board)):
            print("| " + ' '.join([str(v) for v in self._board[i]]))
        
        print("+" + "-" * len(self._board[0]) * 2)
        print("  " + ' '.join([str(i) for i in range(1, 1 + len(self._board[0]))]))

        return 0


    def check_win(self):
        return 0

    def add_piece(self, row_num, player_num):
        return 0
    


    