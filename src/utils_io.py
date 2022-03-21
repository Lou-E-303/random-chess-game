import os
import chess


def print_board(board_to_print):
    print("\n")
    print(board_to_print)
    print("\n")


def print_flipped_board(board_to_print):
    flipped_board = board_to_print.transform(chess.flip_diagonal)
    print_board(flipped_board.transform(chess.flip_anti_diagonal))


def print_game(game_to_print, board):
    game_to_print.headers["Result"] = board.result()
    print(game_to_print)


def save_pgn_to_file(game_to_save, directory):
    new_index = str(len(os.listdir(directory)))
    print(game_to_save, file=open(directory + '/game_' + new_index + '.pgn', 'w'), end="\n\n")


def set_pgn_headers(game, white_player, black_player):
    game.headers["Event"] = "A test chess game"
    game.headers["Site"] = "The CLI"
    game.headers["Date"] = "1st January 1970"
    game.headers["Round"] = "0"
    game.headers["White"] = white_player.name
    game.headers["Black"] = black_player.name

    return game
