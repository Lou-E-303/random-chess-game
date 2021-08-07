import random


def find_random_move(board):
    legal_moves = list(board.legal_moves)
    random_move_index = random.randint(0, len(legal_moves) - 1)
    random_move = legal_moves[random_move_index]
    return random_move
