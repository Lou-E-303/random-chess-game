import utils_move


class AiPlayer:
    def make_move(self, board):
        move = utils_move.find_random_move(board)
        return move
