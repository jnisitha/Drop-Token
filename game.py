from board import board 
from settings import settings
from input_output import GameInputOutput

class Game:
    def __init__(self):
        self.input_output = GameInputOutput()
        
        print("somethin")

    def setup_game(self, settings = (2,4,4,4)):
        print(settings)
        return 0

    def start_game(self):
        print("started game")
        start_choice = self.input_output.present_start_menu()

        if start_choice == 1:
            self.setup_game(self)
        else: #Custom game check
            custom_settings = self.input_output.get_custom_settings()
            self.setup_game(settings = custom_settings)

        return 0

    def update_game(self):
        return 0


    def handle_user_input(self):
        return 0


    def check_win_or_draw(self):
        return 0


new_game = Game()
new_game.start_game()