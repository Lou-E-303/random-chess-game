import utils_game


class AiPlayer:
    def make_move(self, board):
        move = utils_game.find_random_move(board)
        return move
