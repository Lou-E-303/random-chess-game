import chess
import utils_game
import players

output_directory = "./output_pgn/"

white_player = players.get_white_player()
black_player = players.get_black_player()

board = chess.Board()

game = utils_game.setup_game()

utils_game.play_game(game, board, output_directory, white_player, black_player)

