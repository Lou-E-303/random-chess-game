import chess
import utils_game


class AiPlayer:
    def make_move(self, board):
        move = utils_game.find_random_move(board)
        return move


class HumanPlayer:
    def make_move(self, board):
        while True:
            move = self.get_human_move_input(board)
            if utils_game.check_move_is_valid(board, move):
                break
            else:
                print("Move: " + chess.move.uci(move) + " is invalid. Please try again.")
        return move

    def get_human_move_input(self, board):
        selected_move = board.parse_san(input("Please enter a move in algebraic notation: "))
        return selected_move
