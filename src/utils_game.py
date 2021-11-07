import chess.pgn
import utils_io
import random
import players


def setup_game():
    new_game = chess.pgn.Game()
    new_game = utils_io.set_pgn_headers(new_game)
    return new_game


def record_game(game, board, filepath):
    utils_io.print_game(game, board)
    utils_io.print_board(board)
    utils_io.save_pgn_to_file(game, filepath)


def play_game(game, board, filepath, white_player, black_player):
    node = game  # Define root node for game

    while not board.is_game_over():
        # This will need to be more robust to support custom positions
        # type(starting_player)....... and board.turn != starting_colour etc. etc.
        if type(black_player) == players.HumanPlayer and board.turn != chess.WHITE:
            utils_io.print_flipped_board(board)
        else:
            utils_io.print_board(board)

        node = play_next_move(board, white_player, black_player, node)

    record_game(game, board, filepath)


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


def find_random_move(board):
    legal_moves = list(board.legal_moves)
    random_move_index = random.randint(0, len(legal_moves) - 1)
    random_move = legal_moves[random_move_index]
    return random_move


def check_move_is_valid(board, move):
    legal_moves = list(board.legal_moves)
    for legal_move in legal_moves:
        if move == legal_move:
            return True
    return False
