import chess.pgn
import utils_io
import utils_move


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
    utils_io.print_game(game, board)
    utils_io.print_board(board)
    utils_io.save_pgn_to_file(game, filepath)


def play_game(game, board, filepath, white_player, black_player):
    node = game  # Define root node for game

    while not board.is_game_over():
        utils_io.print_board(board)

        node = play_next_move(board, white_player, black_player, node)

    record_game_result(game, board, filepath)


def play_next_move(board, white_player, black_player, node):
    if board.turn == chess.WHITE:
        next_move = white_player.make_move(board)
    elif board.turn == chess.BLACK:
        next_move = black_player.make_move(board)
    else:
        raise ValueError('Somehow, it\'s no-one\'s turn? Not sure how that is possible. Turn: ' + board.turn)

    print("Move Played: ", board.san(next_move))
    board.push(next_move)
    node = node.add_variation(next_move)

    return node
