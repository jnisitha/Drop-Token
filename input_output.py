class GameInputOutput():

    def present_start_menu(self):
        start_choice = input("Please select a game mode: \n 1. Play game \n 2. Custom game \n")
        print("Start choice: " + str(start_choice))
        return start_choice

    def get_custom_settings(self):
        num_players = input("Input number of players: ")
        num_rows = input("Input number of Rows in the board: ")
        num_columns = input("Input number of Columns in the board: ")
        win_condition = input("How many in a row/column/diagonal do you have to get in order to win? ")

        return (num_players, num_rows, num_columns, win_condition)

    
