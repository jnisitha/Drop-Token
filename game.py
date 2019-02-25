import sys
from board import Board
from game_io import GameInputOutput

class Game:
    def __init__(self, num_players = 2, num_rows = 4, num_columns = 4, win_threshold = 4):
        self.num_players = num_players
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.win_threshold = win_threshold
        self.move_history = []
        self.current_player = 1

    def setup_game(self):
        # print("Setting up game")
        start_choice = GameInputOutput.get_start_choice()

        invalid_choice = True
        while invalid_choice:
            #Default settings
            if start_choice == '1':
                invalid_choice = False
            #Custom settings
            elif start_choice == '2': 
                custom_settings = GameInputOutput.get_custom_settings()

                self.num_players = int(custom_settings[0])
                self.num_rows = int(custom_settings[1])
                self.num_columns = int(custom_settings[2])
                self.win_threshold = int(custom_settings[3])
                invalid_choice = False

        self.start_game()

    def next_player(self):
        self.current_player = (self.current_player % self.num_players) + 1

    def start_game(self):
        #print ("Starting game")
        end = False
        
        #create new game board.
        self.board = Board(self.num_rows, self.num_columns)

        #game loop
        while not end:           
            self.handle_player_input()
            won = self.board.check_win(self.win_threshold)

            if won:
                GameInputOutput.print_win_message()
                end = True
            
            self.next_player()

    def handle_put(self, column_num):
        
        current_player = len(self.move_history) % self.num_players + 1
        move_made = self.board.process_move(column_num, current_player)

        if move_made:
            GameInputOutput.print_ok()
            self.move_history.append(column_num)            
        else:
            GameInputOutput.error_message()

    def handle_player_input(self):
        player_input = GameInputOutput.get_player_input()
        command = str(player_input).strip().split()   

        if command[0] == "EXIT":
            sys.exit()
        elif command[0] == "GET":
            GameInputOutput.print_move_history(self.move_history)
        elif command[0] == "PUT":            
            self.handle_put(int(command[1]))
        elif command[0] == "BOARD":
            self.board.print_board()

        return


if __name__ == "__main__":
    new_game = Game()
    new_game.start_game()
