from graphics.board import *


def calculate_best_move(board, player):
    best_score = -float('inf')
    best_move = None

    for row in range(board.ROW):
        for col in range(board.COL):
            if board.board[row][col] == CellStatus.EMPTY:
                board.board[row][col] = player
                score = minimax(board, 5, False, player)
                board.board[row][col] = CellStatus.EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move


def minimax(board, depth, is_maximizing, player):
    if depth == 0 or board.game_result is not None:
        return evaluate(board, player)

    if is_maximizing:
        best_score = -float('inf')
        for row in range(board.ROW):
            for col in range(board.COL):
                if board.board[row][col] == CellStatus.EMPTY:
                    board.board[row][col] = player
                    board.check_win(row, col, player)
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
                    board.check_win(row, col, get_opponent(player))
                    score = minimax(board, depth - 1, True, player)
                    board.board[row][col] = CellStatus.EMPTY
                    best_score = min(score, best_score)
        return best_score


def evaluate(board, player):
    # Define a scoring system based on the number of pieces in a row for the player

    # Scores for different lengths of consecutive pieces
    consecutive_scores = {
        1: 1,      # One piece in a row
        2: 10,     # Two pieces in a row
        3: 100,    # Three pieces in a row
        4: 1000,   # Four pieces in a row
        5: 10000   # Five pieces in a row (winning condition)
    }

    total_score = 0

    # Check horizontal, vertical, and diagonal lines for consecutive pieces
    for row in range(board.ROW):
        for col in range(board.COL):
            if board.board[row][col] == player:
                # Check horizontal
                consecutive_count = 1
                for offset in range(1, board.NEED_TO_WIN):
                    if col + offset >= board.COL or board.board[row][col + offset] != player:
                        break
                    consecutive_count += 1
                total_score += consecutive_scores.get(consecutive_count, 0)

                # Check vertical
                consecutive_count = 1
                for offset in range(1, board.NEED_TO_WIN):
                    if row + offset >= board.ROW or board.board[row + offset][col] != player:
                        break
                    consecutive_count += 1
                total_score += consecutive_scores.get(consecutive_count, 0)

                # Check diagonal (top-left to bottom-right)
                consecutive_count = 1
                for offset in range(1, board.NEED_TO_WIN):
                    if col + offset >= board.COL or row + offset >= board.ROW or board.board[row + offset][col + offset] != player:
                        break
                    consecutive_count += 1
                total_score += consecutive_scores.get(consecutive_count, 0)

                # Check diagonal (top-right to bottom-left)
                consecutive_count = 1
                for offset in range(1, board.NEED_TO_WIN):
                    if col - offset < 0 or row + offset >= board.ROW or board.board[row + offset][col - offset] != player:
                        break
                    consecutive_count += 1
                total_score += consecutive_scores.get(consecutive_count, 0)

    return total_score

def get_opponent(player):
    return CellStatus.CIRCLE if player == CellStatus.CROSS else CellStatus.CROSS


# Example usage:
if __name__ == "__main__":
    game_board = Board()
    player = CellStatus.CROSS
    best_move = calculate_best_move(game_board, player)
    print(f"The best move for {player} is {best_move}")
