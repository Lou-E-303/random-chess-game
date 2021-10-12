def print_board(board_to_print):
    print("\n")
    print(board_to_print)
    print("\n")


def print_game(game_to_print, board):
    game_to_print.headers["Result"] = board.result()
    print(game_to_print)


def save_pgn_to_file(game_to_save, filepath):
    print(game_to_save, file=open(filepath, "w"), end="\n\n")


def set_pgn_headers(game):
    game.headers["Event"] = "A test chess game with random moves"
    game.headers["Site"] = "The CLI"
    game.headers["Date"] = "1st January 1970"
    game.headers["Round"] = ""
    game.headers["White"] = ""
    game.headers["Black"] = ""

    return game
