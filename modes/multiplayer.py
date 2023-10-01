from graphics.board import *


def start_playing_with_friend():
    main_board = Board()

    whats_turn = CellStatus.CROSS

    for i in range(main_board.ROW * main_board.COL):

        print(main_board)
        print("Ход " + whats_turn.value)
        print("Сделайте ход написав координаты. Пример 'H10'")

        while True:
            turn = main_board.convert_coordinates(input("Ход " + whats_turn.value + " в ячейку:"))
            if main_board.add_move(turn, whats_turn):
                break

        if main_board.check_win():
            print(main_board)
            break

        whats_turn = CellStatus.CIRCLE if whats_turn == CellStatus.CROSS else CellStatus.CROSS
    else:
        print("Ничья!")

    print("ПОБЕДИЛА КОМАНДА", main_board.game_result.value())
    input("Нажмите ENTER чтобы вернуться в меню ")
