import chess.pgn
import utils_io
import random
import players


def setup_game():
    new_game = chess.pgn.Game()
    new_game = utils_io.set_pgn_headers(new_game)
    return new_game


def record_game_result(game, board, filepath):
    utils_io.print_game(game, board)
    utils_io.print_board(board)
    utils_io.save_pgn_to_file(game, filepath)


def play_game(game, board, filepath, white_player, black_player):
    node = game  # Define root node for game

    while not board.is_game_over():
        print("DEBUG: Ply = ", board.ply())
        # if check_for_human_players_turn(board, white_player, black_player) and board.ply() > 0:
        #     utils_io.print_flipped_board(board)
        # else:
        #     utils_io.print_board(board)

        if check_for_computer_game(white_player, black_player) or board.ply() == 0:
            utils_io.print_board(board)
        else:
            utils_io.print_flipped_board(board)

        node = play_next_move(board, white_player, black_player, node)

    record_game_result(game, board, filepath)


def check_for_human_players_turn(board, white_player, black_player):
    human_players_turn = False

    if board.turn == chess.WHITE and type(white_player) is players.HumanPlayer:
        print("White to play.")
        human_players_turn = True
    elif board.turn == chess.BLACK and type(black_player) is players.HumanPlayer:
        print("Black to play.")
        human_players_turn = True

    return human_players_turn

def check_for_computer_game(white_player, black_player):
    if type(white_player) == players.AiPlayer and type(black_player) == players.AiPlayer:
        return True
    else:
        return False


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
