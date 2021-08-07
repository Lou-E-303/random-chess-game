def print_board(board_to_print):
    print("\n")
    print(board_to_print)
    print("\n")


def print_game(game_to_print, board):
    game_to_print.headers["Result"] = board.result()
    print(game_to_print)