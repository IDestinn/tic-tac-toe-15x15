import math

def calculate_best_move(board, player):
    best_score = -math.inf
    best_move = None

    for row in range(board.ROW):
        for col in range(board.COL):
            if board.is_valid_move(row, col):
                board.make_move(row, col, player)
                score = minimax(board, 0, False, -math.inf, math.inf, player)
                board.undo_move(row, col)  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def minimax(board, depth, is_maximizing, alpha, beta, player):
    if depth == MAX_DEPTH or board.is_game_over():
        return evaluate(board, player)

    if is_maximizing:
        best_score = -math.inf
        for row in range(board.ROW):
            for col in range(board.COL):
                if board.is_valid_move(row, col):
                    board.make_move(row, col, player)
                    score = minimax(board, depth + 1, False, alpha, beta, player)
                    board.undo_move(row, col)  # Undo the move
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(board.ROW):
            for col in range(board.COL):
                if board.is_valid_move(row, col):
                    board.make_move(row, col, get_opponent(player))
                    score = minimax(board, depth + 1, True, alpha, beta, player)
                    board.undo_move(row, col)  # Undo the move
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def evaluate(board, player):
    # Implement your evaluation function here
    # This function should return a score indicating the strength of the board state for the given player
    # You can consider factors like the number of pieces in a row, potential threats, and opportunities for the player

    # For a simple prototype, you can return a random score
    import random
    return random.randint(0, 10)

def get_opponent(player):
    return "X" if player == "O" else "O"
