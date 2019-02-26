class GameInputOutput:
    @staticmethod
    def get_start_choice():
        '''Presents player with default or custom settings options.'''
        start_choice = input("Please select a game mode: \n 1. Play game \n 2. Custom game \n")
        print("Start choice: " + start_choice)
        return start_choice

    @staticmethod
    def get_custom_settings():
        '''Guides player through custom game set-up.'''
        num_players = input("Input number of players: ")
        num_rows = input("Input number of Rows in the board: ")
        num_columns = input("Input number of Columns in the board: ")
        win_threshold = input("How many in a row/column/diagonal do you have to get in order to win? ")
        return num_players, num_rows, num_columns, win_threshold

    @staticmethod
    def get_player_input():
        '''Waiting for player input.'''
        command = input("")
        return command

    @staticmethod
    def print_error_message():
        '''Prints error message.'''
        print("ERROR")
        return 0

    @staticmethod
    def print_win_message():
        '''Prints WIN.'''
        print("WIN")

    @staticmethod
    def print_draw_message():
        '''Print DRAW'''
        print("DRAW")

    @staticmethod
    def print_ok():
        '''Prints OK'''
        print("OK")

    @staticmethod
    def print_move_history(move_history):
        '''Prints the move history.'''
        for i in range(len(move_history)):
            print(move_history[i])

    @staticmethod
    def print_board(board):
        '''Prints the game board.'''
        for i in range(len(board)):
            print("| " + ' '.join([str(v) for v in board[i]]))

        print("+" + "-" * len(board[0]) * 2)
        print("  " + ' '.join([str(i) for i in range(1, 1 + len(board[0]))]))
