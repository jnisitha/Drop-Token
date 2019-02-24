import sys
from board import Board 
from settings import settings
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
        print("setting up game")
        start_choice = self.input_output.present_start_menu()

        #default settings
        if start_choice == 1: 
            self.start_game()
        #Custom settings
        elif start_choice == 2: 
            custom_settings = self.input_output.get_custom_settings()

            #Custom settings:
            self.num_players = custom_settings[0]
            self.num_rows = custom_settings[1]
            self.num_columns = custom_settings[2]
            self.win_condition = custom_settings[3]

            self.start_game()
        else: #if input is wrong show error and present game menu.
            self.input_output.error_message()
            start_choice = self.input_output.present_start_menu()

        return 0

    def start_game(self):
        print ("starting game")
        end = False
        move_number = 1
        board = Board(self.num_rows, self.num_columns)
        # while !end:
        #     current_player = move_number % self.num_players + 1
        #     player_input = self.input_output.player_input(current_player)
        #     self.handle_player_input(player_input)

        return 0
        

    def update_game(self):
        return 0


    def handle_player_input(self, player_input):
        if player_input == "EXIT":
            sys.exit()
        elif player_input == "GET":
            print(self.move_history)
        elif type(player_input) == int:
            print("blah")
            
        return 0


    def check_win_or_draw(self, move):

        # for x in range(self.win_condition):
        #     for y in (self.win_condition):
                
        return 0


new_game = Game()
new_game.setup_game()