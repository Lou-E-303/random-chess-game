import chess
import chess.pgn
import random


def setup_game():
    new_game = chess.pgn.Game()
    game.headers["Event"] = "A test chess game with random moves"
    game.headers["Site"] = "The CLI"
    game.headers["Date"] = "1st January 1970"
    game.headers["Round"] = ""
    game.headers["White"] = ""
    game.headers["Black"] = ""
    return new_game


def print_board(board_to_print):
    print("\n")
    print(board_to_print)
    print("\n")


def print_game(game_to_print):
    game.headers["Result"] = board.result()
    print(game_to_print)


board = chess.Board()

node = game = setup_game()

while True:
    print_board(board)
    legalMoves = list(board.legal_moves)
    randomMoveIndex = random.randint(0, len(legalMoves) - 1)
    randomMove = legalMoves[randomMoveIndex]
    print("Move Played: ", board.san(randomMove))
    board.push(randomMove)
    node = node.add_variation(randomMove)
    if board.is_checkmate():
        print("Checkmate!")
        print_game(game, board)
        print_board(board)
        break
    elif board.is_stalemate():
        print("Stalemate!")
        print_game(game, board)
        print_board(board)
        break
    elif board.is_insufficient_material():
        print("Insufficient material!")
        print_game(game, board)
        print_board(board)
        break
