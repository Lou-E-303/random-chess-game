import chess
import utils_game
import players

output_directory = "./output_pgn/"

white_player = players.get_player_for_colour("White")
black_player = players.get_player_for_colour("Black")

board = chess.Board()

game = utils_game.setup_game(white_player, black_player)

utils_game.play_game(game, board, output_directory, white_player, black_player)

