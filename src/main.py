import chess

import utils_io
import utils_game
import utils_move

output_directory = "./src/output_pgn/"
output_filename = "test.pgn"

board = chess.Board()

node = game = utils_game.setup_game()

while not board.is_game_over():
    utils_io.print_board(board)

    random_move = utils_move.find_random_move(board)
    print("Move Played: ", board.san(random_move))
    board.push(random_move)
    node = node.add_variation(random_move)

result = utils_game.record_game_result(game, board, output_directory + output_filename)