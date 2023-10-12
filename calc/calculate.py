import modes.trainmode
from gui import CellStatus, Board


# Cross in +inf
# Circle in -inf
def calculate_best_move(given_board: Board, player_side: CellStatus):
    DEPTH = given_board.ROW * given_board.COL
    best_score = -float('inf') if player_side == CellStatus.CROSS else float('inf')
    best_move = None
    # Выбираем противоположную сторону для хода соперника
    is_max = False if player_side == CellStatus.CROSS else True
    for row, col in given_board.get_valid_moves():
        given_board.add_move(row, col, player_side)
        cur_score = minimax(given_board, DEPTH, -float('inf'), float('inf'), is_max)
        given_board.remove_move(row, col)

        if cur_score > best_score:
            best_score = cur_score
            best_move = (row, col)

    return best_move


def minimax(analyzing_board: Board, depth, alpha, beta, maximizing_player):
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


def evaluate(eval_board: Board):
    if eval_board.game_result == CellStatus.CROSS:
        return 1
    if eval_board.game_result == CellStatus.CIRCLE:
        return -1
    return 0


if __name__ == "__main__":
    modes.start_training_bots(3, 3, 3)
