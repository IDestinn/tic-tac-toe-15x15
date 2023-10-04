from enum import Enum


class CellStatus(Enum):
    EMPTY = " "
    CROSS = "X"
    CIRCLE = "O"


class Board:

    def __init__(self, row=15, col=15, need_to_win=5) -> None:
        self.ROW = row
        self.COL = col
        self.NEED_TO_WIN = need_to_win
        self.board = [[CellStatus.EMPTY for _ in range(self.COL)] for _ in range(self.ROW)]
        self.game_result = None
        self.last_move = (None, None, None)

    def __str__(self) -> str:
        board_str = "  ┌" + "───┬" * (self.COL - 1) + "───┐\n"

        for i in range(self.ROW):
            num_of_row = self.ROW - i
            row = str(num_of_row) + "│" if num_of_row >= 10 else " " + str(num_of_row) + "│"

            for j in range(self.COL):
                row += " " + self.board[i][j].value + " │"
            board_str += row + "\n"

            if i < self.ROW - 1:
                board_str += "  ├" + "───┼" * (self.COL - 1) + "───┤\n"

        board_str += "  └" + "───┴" * (self.COL - 1) + "───┘\n"
        board_str += "    " + "   ".join(chr(ord('A') + i) for i in range(self.COL))

        return board_str

    def get_valid_moves(self):
        return [(i, j) for i, inner_array in enumerate(self.board)
                for j, element in enumerate(inner_array) if element == CellStatus.EMPTY]

    def convert_coord_to_index(self, player_input) -> [int, int]:
        col = int(ord(player_input[0].upper()) - ord('A'))
        row = self.ROW - int(player_input[1:])
        return col, row

    def convert_index_to_coord(self, row, col) -> str | None:
        if 0 <= row < self.ROW and 0 <= col < self.COL:
            return chr(ord('A') + col) + str(self.ROW - row)
        return

    def add_player_move(self, player_input, player) -> bool:
        if not (2 <= len(player_input) <= 3):
            print("Координаты записаны неверно")
            return False

        col_str = player_input[0]
        row_str = player_input[1:]

        if not 'A' <= col_str.upper() <= chr(ord('A') + self.COL - 1):
            print("Координаты записаны неверно")
            return False

        try:
            row = int(row_str)
            if not 1 <= row <= self.ROW:
                print("Координаты записаны неверно")
                return False
        except ValueError:
            print("Координаты записаны неверно")
            return False

        col, row = self.convert_coord_to_index(player_input)

        if player not in CellStatus:
            print("Ошибка с определением символа")
            return False

        if self.board[row][col] != CellStatus.EMPTY:
            print("Клетка уже занята")
            return False

        self.board[row][col] = player
        self.last_move = (player, row, col)
        return True

    def add_ai_move(self, row, col, player):
        self.board[row][col] = player
        self.last_move = (player, row, col)

    def remove_move(self):
        self.board[self.last_move[1]][self.last_move[2]] = self.last_move[0]

    def check_win(self) -> bool:
        row = self.last_move[1]
        col = self.last_move[2]
        player = self.last_move[0]
        # Проверяет горизонтальное направление
        if self.check_line(row, col, 0, 1, player) + self.check_line(row, col, 0, -1, player) >= self.NEED_TO_WIN - 1:
            self.game_result = player
            return True

        # Проверяет вертикальное направление
        if self.check_line(row, col, 1, 0, player) + self.check_line(row, col, -1, 0, player) >= self.NEED_TO_WIN - 1:
            self.game_result = player
            return True

        #  Проверяет диагональное направление (с левого-верхнего до правого-нижнего)
        if self.check_line(row, col, 1, 1, player) + self.check_line(row, col, -1, -1, player) >= self.NEED_TO_WIN - 1:
            self.game_result = player
            return True

        # Проверяет диагональное направление (с левого-нижнего до правого-верхнего)
        if self.check_line(row, col, 1, -1, player) + self.check_line(row, col, -1, 1, player) >= self.NEED_TO_WIN - 1:
            self.game_result = player
            return True

        return False

    def check_line(self, row, col, row_directory, column_directory, player) -> int:
        count = 0
        row, col = row + row_directory, col + column_directory
        while 0 <= row < self.ROW and 0 <= col < self.COL and self.board[row][col] == player:
            count += 1
            row += row_directory
            col += column_directory
        return count

    def in_field(self, row, col) -> bool:
        return 0 <= row < self.ROW and 0 <= col < self.COL


if __name__ == "__main__":
    board = Board()

    board.add_player_move("G7", CellStatus.CROSS)
    board.add_player_move("H5", CellStatus.CIRCLE)
    board.add_player_move("A5", CellStatus.CROSS)
    board.add_player_move("O15", CellStatus.CIRCLE)
    board.add_player_move("A1", CellStatus.CROSS)
    board.add_player_move("A15", CellStatus.CIRCLE)
    board.add_player_move("O1", CellStatus.CROSS)
    print(board.convert_index_to_coord(6, 7))

    board.add_player_move("!!", CellStatus.CIRCLE)

    print(board)
