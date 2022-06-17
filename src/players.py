import utils_game


class AiPlayer:
    name = "AI Player"

    def make_move(self, board):
        move = utils_game.find_random_move(board)
        return move


class HumanPlayer:
    name = "Human Player"

    def make_move(self, board):
        while True:
            move = self.get_human_move_input()
            if utils_game.check_move_is_valid(board, move):
                break
            else:
                print("Move " + move + " is invalid. Please try again.")
        return board.parse_san(move)

    def get_human_move_input(self):
        selected_move = input("Please enter a move in algebraic notation: ")
        return selected_move


def get_player_for_colour(colour):
    if input("Should a human play %s? Enter Y for Yes or N for No: " % colour).upper() == "Y":
        return HumanPlayer()
    else:
        return AiPlayer()
