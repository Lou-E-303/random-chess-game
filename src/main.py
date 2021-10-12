import chess
import utils_game
import players

output_directory = "./src/output_pgn/"
output_filename = "test.pgn"

white_player = players.AiPlayer()
black_player = players.HumanPlayer()

board = chess.Board()

game = utils_game.setup_game()

utils_game.play_game(game, board, output_directory + output_filename, white_player, black_player)

