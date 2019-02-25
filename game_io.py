class GameInputOutput:

    def get_start_choice():
        start_choice = input("Please select a game mode: \n 1. Play game \n 2. Custom game \n")
        print("Start choice: " + start_choice)
        return start_choice

    def get_custom_settings():
        num_players = input("Input number of players: ")
        num_rows = input("Input number of Rows in the board: ")
        num_columns = input("Input number of Columns in the board: ")
        win_threshold = input("How many in a row/column/diagonal do you have to get in order to win? ")

        return (num_players, num_rows, num_columns, win_threshold)

    def print_error_message():
        print("ERROR")
        return 0

    def get_player_input():
        
        command = input("")
        return command

    def print_win_message():
        print("WIN")
    
    def print_ok():
        print("OK")
    
    def print_move_history(move_history):
        print(move_history)

    def print_board(board):        
        for i in range(len(board)):
            print("| " + ' '.join([str(v) for v in board[i]]))
        
        print("+" + "-" * len(board[0]) * 2)
        print("  " + ' '.join([str(i) for i in range(1, 1 + len(board[0]))]))
