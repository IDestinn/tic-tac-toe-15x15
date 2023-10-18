from gui import Board, CellStatus

start_board = Board(3, 3, 3)
game_results = {"Ничья": 0, "Победа Х": 0, "Победа О": 0}

whats_turn = CellStatus.CROSS

def test(test_board: Board, row = -1, col = -1):
    global whats_turn
    global game_results
    if row != -1 and col != -1:
        test_board.add_move(row, col, whats_turn)
        if test_board.check_win(row, col, whats_turn):
                game_results["Победа О"] += 1
                return
        whats_turn = CellStatus.CIRCLE if whats_turn == CellStatus.CROSS else CellStatus.CROSS
    for i in range(len(test_board.get_valid_moves())):
        
        if whats_turn == CellStatus.CROSS:
            ai_move = test_board.add_ai_move(whats_turn)

            if test_board.check_win(ai_move[0], ai_move[1], whats_turn):
                game_results["Победа Х"] += 1
                break
        else:
            for (row, col) in test_board.get_valid_moves():
                test(test_board, row, col)

        whats_turn = CellStatus.CIRCLE if whats_turn == CellStatus.CROSS else CellStatus.CROSS
    else:
        game_results["Ничья"] += 1

test(start_board)
print(game_results)