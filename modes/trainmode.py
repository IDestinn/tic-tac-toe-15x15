from graphics.board import *
import random
import os


def start_training_bots(rows=15, cols=15, need_to_win=5):
    main_board = Board(rows, cols, need_to_win)

    whats_turn = CellStatus.CROSS

    for i in range(main_board.ROW * main_board.COL):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_board)

        main_board.add_ai_move(whats_turn)

        if main_board.check_win():
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
