from graphics.board import Board, CellStatus, TurnStatus


def calculate_best_move(board, player):
    best_score = -float('inf')
    best_move = None

    for row in range(board.ROW):
        for col in range(board.COL):
            if board.board[row][col] == CellStatus.EMPTY:
                board.board[row][col] = player
                score = minimax(board, 0, False, player)
                board.board[row][col] = CellStatus.EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move


def minimax(board, depth, is_maximizing, player):
    if depth == 0 or board.is_game_over():
        return evaluate(board, player)

    if is_maximizing:
        best_score = -float('inf')
        for row in range(board.ROW):
            for col in range(board.COL):
                if board.board[row][col] == CellStatus.EMPTY:
                    board.board[row][col] = player
                    score = minimax(board, depth - 1, False, player)
                    board.board[row][col] = CellStatus.EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(board.ROW):
            for col in range(board.COL):
                if board.board[row][col] == CellStatus.EMPTY:
                    board.board[row][col] = get_opponent(player)
                    score = minimax(board, depth - 1, True, player)
                    board.board[row][col] = CellStatus.EMPTY
                    best_score = min(score, best_score)
        return best_score


def evaluate(board, player):
    # Implement your evaluation function here
    # This function should return a score indicating the strength of the board state for the given player
    # You can consider factors like the number of pieces in a row, potential threats, and opportunities for the player

    # For a simple prototype, you can return a random score
    import random
    return random.randint(0, 10)


def get_opponent(player):
    return CellStatus.CIRCLE if player == CellStatus.CROSS else CellStatus.CROSS


# Example usage:
if __name__ == "__main__":
    game_board = Board()
    player = CellStatus.CROSS
    best_move = calculate_best_move(game_board, player)
    print(f"The best move for {player} is {best_move}")
