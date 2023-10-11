from gui.board import *
import random
import inquirer
import os


def start_game_with_bot(rows=15, cols=15, need_to_win=5):
    main_board = Board(rows, cols, need_to_win)
    player_char = inquirer.list_input("Кто первый ходит?",
                                      choices=["Бот", "Игрок"])
    player_turn = CellStatus.CROSS if player_char == "Игрок" else CellStatus.CIRCLE
    whats_turn = CellStatus.CROSS

    for i in range(main_board.ROW * main_board.COL):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(main_board)

        print("Ход " + whats_turn.value)
        if whats_turn == player_turn:
            random_cell = random.choice(main_board.get_valid_moves())
            print("Сделайте ход написав координаты. Пример '" +
                  main_board.convert_index_to_coord(random_cell[0], random_cell[1]) + "'")

            while True:
                turn = input("Ход " + whats_turn.value + " в ячейку:")
                if main_board.add_player_move(turn, whats_turn):
                    break
            row, col = main_board.convert_coord_to_index(turn)
            
        else:
            ai_move = main_board.add_ai_move(whats_turn)
            row, col = ai_move[0], ai_move[1]

        if main_board.check_win(row, col, whats_turn):
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
