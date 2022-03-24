import chess.pgn
import random
import utils_io
import players


def setup_game(white_player, black_player):
    new_game = chess.pgn.Game()
    new_game = utils_io.set_pgn_headers(new_game, white_player, black_player)
    return new_game


def record_game(game, board, filepath):
    utils_io.print_game(game, board)
    utils_io.print_board(board)
    utils_io.save_pgn_to_file(game, filepath)


def play_game(game, board, filepath, white_player, black_player):
    node = game  # Define root node for game
    starting_player = white_player  # These exist to eventually support position imports
    starting_colour = chess.WHITE   # i.e. importing a FEN and playing on from the position

    while not board.is_game_over():
        if type(starting_player) == players.HumanPlayer and board.turn != starting_colour:
            utils_io.print_flipped_board(board)
        else:
            utils_io.print_board(board)

        node = play_next_move(board, white_player, black_player, node)

    record_game(game, board, filepath)


def play_next_move(board, white_player, black_player, node):
    if board.turn == chess.WHITE:
        next_move = white_player.make_move(board)
    else:
        next_move = black_player.make_move(board)

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
        if move == board.san(legal_move):
            return True
    return False
