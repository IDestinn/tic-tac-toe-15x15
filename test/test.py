from gui import Board, CellStatus

def test_all_possible_results(board: Board, player_turn: bool, game_results):
    winner = board.game_result
    
    if winner == CellStatus.CROSS:
        game_results["Победа Х"] += 1
    elif winner == CellStatus.CIRCLE:
        game_results["Победа О"] += 1
    elif winner == None and board.get_valid_moves() == []:
        game_results["Ничья"] += 1
    else:
        for row, col in board.get_valid_moves():
            if player_turn:
                board.add_move(row, col, CellStatus.CIRCLE)
            else:
                ai_move = board.add_ai_move(CellStatus.CROSS)
                row, col = ai_move[0], ai_move[1]
                board.add_move(row, col, CellStatus.CROSS)

            test_all_possible_results(board, not player_turn, game_results)

            board.remove_move(row, col)

# Create the initial board
start_board = Board(3, 3, 3)
game_results = {"Ничья": 0, "Победа Х": 0, "Победа О": 0}

# Start the testing with AI playing Cross (X) and player playing Circle (O)
test_all_possible_results(start_board, False, game_results)

# Print the results
print(game_results)
