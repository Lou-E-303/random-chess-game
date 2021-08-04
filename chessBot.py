import chess
import chess.pgn
import random
import time

def print_board(board):
	print("\n")
	print(board)
	print("\n")

def setup_game():
	game = chess.pgn.Game()
	game.headers["Event"] = "A test chess game with random moves"
	game.headers["Site"] = "The CLI"
	game.headers["Date"] = "1st January 1970"
	game.headers["Round"] = ""
	game.headers["White"] = ""
	game.headers["Black"] = ""
	return game

def print_game(game, board):
	game.headers["Result"] = board.result()
	print(game)
	print_board(board)

board = chess.Board()

node = game = setup_game()

while True:
	print_board(board)
	#time.sleep(1)
	legalMoves = list(board.legal_moves)
	randomMoveIndex = random.randint(0, len(legalMoves) - 1)
	randomMove = legalMoves[randomMoveIndex]
	print("Move Played: ", board.san(randomMove))
	board.push(randomMove)
	node = node.add_variation(randomMove)
	if (board.is_checkmate()):
		print("Checkmate, my good bitch")
		print_game(game, board)
		break
	elif (board.is_stalemate()):
		print("Stalemate!")
		print_game(game, board)
		break
	elif (board.is_insufficient_material()):
		print("Insufficient material!")
		print_game(game, board)
		break
