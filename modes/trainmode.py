import os
from gui import Board, CellStatus
from calc.calculate import add_ai_move

def start_training_bots(rows:int=3, cols:int=3, need_to_win:int=3) -> None:
    main_board = Board(rows, cols, need_to_win)

    whats_turn = CellStatus.CROSS

    for i in range(main_board.row * main_board.col):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_board)

        ai_move = add_ai_move(main_board, whats_turn)

        if main_board.check_win(ai_move[0], ai_move[1], whats_turn):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(main_board)
            break

        whats_turn = CellStatus.CIRCLE if whats_turn == CellStatus.CROSS else CellStatus.CROSS
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_board)
        print("Ничья!")

    if main_board.game_result is not None:
        print("ПОБЕДИЛА КОМАНДА", main_board.game_result.value)
    input("Нажмите ENTER чтобы вернуться в меню ")
