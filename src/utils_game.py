import chess.pgn
import utils_io


def setup_game():
    new_game = chess.pgn.Game()
    new_game.headers["Event"] = "A test chess game with random moves"
    new_game.headers["Site"] = "The CLI"
    new_game.headers["Date"] = "1st January 1970"
    new_game.headers["Round"] = ""
    new_game.headers["White"] = ""
    new_game.headers["Black"] = ""
    return new_game


def record_game_result(game, board, filepath):
    if board.is_checkmate():
        print("Checkmate!")
        utils_io.print_game(game, board)
        utils_io.print_board(board)
        utils_io.save_pgn_to_file(game, filepath)

    elif board.is_stalemate():
        print("Stalemate!")
        utils_io.print_game(game, board)
        utils_io.print_board(board)
        utils_io.save_pgn_to_file(game, filepath)

    elif board.is_insufficient_material():
        print("Insufficient material!")
        utils_io.print_game(game, board)
        utils_io.print_board(board)
        utils_io.save_pgn_to_file(game, filepath)
