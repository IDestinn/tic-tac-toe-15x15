from gui.board import CellStatus


def evaluate(eval_board):
    if eval_board.game_result == CellStatus.CROSS:
        return 1
    if eval_board.game_result == CellStatus.CIRCLE:
        return -1
    return 0
    # Define a scoring system based on the number of pieces in a row for the player

    # Scores for different lengths of consecutive pieces
    # consecutive_scores = {i + 1 : 10**i  for i in range(eval_board.NEED_TO_WIN)}

    # eval_player = CellStatus.CROSS if maximizing_player else CellStatus.CIRCLE
    # total_score = 0

    # # Check horizontal, vertical, and diagonal lines for consecutive pieces
    # for row in range(eval_board.ROW):
    #     for col in range(eval_board.COL):
    #         if eval_board.board[row][col] == eval_player:
    #             # Check horizontal
    #             consecutive_count = 1
    #             for offset in range(1, eval_board.NEED_TO_WIN):
    #                 if col + offset >= eval_board.COL or eval_board.board[row][col + offset] != eval_player:
    #                     break
    #                 consecutive_count += 1
    #             total_score += consecutive_scores.get(consecutive_count, 0)

    #             # Check vertical
    #             consecutive_count = 1
    #             for offset in range(1, eval_board.NEED_TO_WIN):
    #                 if row + offset >= eval_board.ROW or eval_board.board[row + offset][col] != eval_player:
    #                     break
    #                 consecutive_count += 1
    #             total_score += consecutive_scores.get(consecutive_count, 0)

    #             # Check diagonal (top-left to bottom-right)
    #             consecutive_count = 1
    #             for offset in range(1, eval_board.NEED_TO_WIN):
    #                 if (col + offset >= eval_board.COL or row + offset >= eval_board.ROW
    #                         or eval_board.board[row + offset][col + offset] != eval_player):
    #                     break
    #                 consecutive_count += 1
    #             total_score += consecutive_scores.get(consecutive_count, 0)

    #             # Check diagonal (top-right to bottom-left)
    #             consecutive_count = 1
    #             for offset in range(1, eval_board.NEED_TO_WIN):
    #                 if (col - offset < 0 or row + offset >= eval_board.ROW
    #                         or eval_board.board[row + offset][col - offset] != eval_player):
    #                     break
    #                 consecutive_count += 1
    #             total_score += consecutive_scores.get(consecutive_count, 0)
