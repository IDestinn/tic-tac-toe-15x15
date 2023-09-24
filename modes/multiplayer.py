from graphics.board import *


def start_playing_with_friend():
    print("Начинается игра с другом...")

    main_board = Board()

    whats_turn = CellStatus.CROSS

    for i in range(main_board.ROW * main_board.COL):

        print(main_board)
        print("Ход " + whats_turn.value)
        print("Сделайте ход написав координаты. Пример 'H10'")

        while True:
            turn = input("Ход " + whats_turn.value + " в ячейку:")
            result = main_board.add_move(turn, whats_turn)
            if result != TurnStatus.ERROR:
                break

        if result == TurnStatus.WIN:
            print(main_board)
            break

        whats_turn = CellStatus.CIRCLE if whats_turn == CellStatus.CROSS else CellStatus.CROSS
    else:
        print("Ничья!")

    print("ПОБЕДИЛА КОМАНДА", whats_turn.value)
    input("Нажмите ENTER чтобы вернуться в меню ")
