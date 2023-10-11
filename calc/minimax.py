from calc.eval import evaluate
from gui.board import CellStatus


def minimax(analyzing_board, depth, alpha, beta, maximizing_player):
    if depth == 0 or analyzing_board.game_result is not None:
        return evaluate(analyzing_board)

    if maximizing_player:
        best_score = -float('inf')
        for row, col in analyzing_board.get_valid_moves():
            analyzing_board.add_move(row, col, CellStatus.CROSS)
            analyzing_board.check_win(row, col, CellStatus.CROSS)
            score = minimax(analyzing_board, depth - 1, alpha, beta, False)
            alpha = max(alpha, score)
            analyzing_board.remove_move(row, col)
            best_score = max(score, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for row, col in analyzing_board.get_valid_moves():
            analyzing_board.add_move(row, col, CellStatus.CIRCLE)
            analyzing_board.check_win(row, col, CellStatus.CIRCLE)
            score = minimax(analyzing_board, depth - 1, alpha, beta, True)
            beta = min(beta, score)
            analyzing_board.remove_move(row, col)
            best_score = min(score, best_score)
            if beta <= alpha:
                break
        return best_score
