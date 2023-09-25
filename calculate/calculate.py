import math


def best_move(board, is_maximaze) -> [int, int]:
    pass


def minimax(board, depth, alpha, beta, maximizing_player) -> int:
    if depth == 0 or board.check_win(row, col, player):
        return evaluetion(row, col)
    
    if maximizing_player:
        max_eval = -math.inf
        for row in board.ROW:
            for col in board.COL:
                if board[row][col] != CellStatus.EMPTY:
                    eval = minimax(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        max_eval = math.inf
        for row in board.ROW:
            for col in board.COL:
                if board[row][col] != CellStatus.EMPTY:
                    eval = minimax(child, depth - 1, alpha, beta, True)
                max_eval = max(max_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return max_eval
    
def evaluation() -> int:
    pass