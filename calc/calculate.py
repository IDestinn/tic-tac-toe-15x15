import modes.trainmode
from calc.minimax import minimax
from gui.board import *


# Cross in +inf
# Circle in -inf

def calculate_best_move(given_board, player_side):
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


if __name__ == "__main__":
    modes.start_training_bots()
