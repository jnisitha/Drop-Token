import sys
from board import Board
from input_output import GameInputOutput

class Game:
    def __init__(self):
        self.input_output = GameInputOutput()
        self.num_players = 2
        self.num_rows = 4
        self.num_columns = 4
        self.win_condition = 4
        self.move_history = []

    def setup_game(self):
        print("Setting up game")
        start_choice = self.input_output.present_start_menu()

        #default settings
        if start_choice == '1': 
            self.start_game()
        #Custom settings
        elif start_choice == '2': 
            custom_settings = self.input_output.get_custom_settings()

            #Custom settings:
            self.num_players = int(custom_settings[0])
            self.num_rows = int(custom_settings[1])
            self.num_columns = int(custom_settings[2])
            self.win_condition = int(custom_settings[3])

            self.start_game()
        else: #if input is wrong show error and present game menu.
            self.input_output.error_message()
            start_choice = self.input_output.present_start_menu()

        return 0

    def start_game(self):
        print ("Starting game")
        end = False
        
        #create new game board.
        self.board = Board(self.num_rows, self.num_columns)

        #game loop
        while end == False:
            current_player = len(self.move_history) % self.num_players + 1
            player_input = self.input_output.player_input()
            won = self.handle_player_input(player_input, current_player)
            
            if won:
                self.input_output.win_message()
                end = True
            
        return
        

    def update_game(self):
        return 0


    def handle_player_input(self, player_input, current_player):
        command = str(player_input).strip().split(' ')
        

        if command[0] == "EXIT":
            sys.exit()
        elif command[0] == "GET":
            print(self.move_history)
        elif command[0] == "PUT":
            #print("processing move " + command[1])
            column_num = int(command[1]) - 1

            move_made = self.board.process_move(column_num, current_player)
            if move_made:
                self.input_output.print_ok()
                self.move_history.append(command[1])
                won = self.board.check_win(self.win_condition)
                return won 
            else:
                self.input_output.error_message()
                
        elif command[0] == "BOARD":
            self.board.print_board()

        return


new_game = Game()
new_game.setup_game()