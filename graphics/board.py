from enum import Enum


class CellStatus(Enum):
    EMPTY = " "
    CROSS = "X"
    CIRCLE = "O"


class TurnStatus(Enum):
    ERROR = -1
    TURN = 0
    WIN = 1


class Board:

    def __init__(self, row=15, col=15, need_to_win=5) -> None:
        self.ROW = row
        self.COL = col
        self.NEED_TO_WIN = need_to_win
        self.board = [[CellStatus.EMPTY for _ in range(self.COL)] for _ in range(self.ROW)]

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

    def is_valid(self, player_input) -> bool:
        if not (2 <= len(player_input) <= 3):
            return False

        col_str = player_input[0]
        row_str = player_input[1:]

        if not 'A' <= col_str.upper() <= chr(ord('A') + self.COL - 1):
            return False

        try:
            row = int(row_str)
            if not 1 <= row <= self.ROW:
                return False
        except ValueError:
            return False

        return True

    def convert_coordinates(self, player_input):
        col = int(ord(player_input[0].upper()) - ord('A'))
        row = self.ROW - int(player_input[1:])
        return col, row

    def add_move(self, player_input, player) -> TurnStatus:
        if not self.is_valid(player_input):
            print("Координаты записаны неверно")
            return TurnStatus.ERROR

        col, row = self.convert_coordinates(player_input)

        if player not in CellStatus:
            print("Ошибка с определением символа")
            return TurnStatus.ERROR

        if self.board[row][col] != CellStatus.EMPTY:
            print("Клетка уже занята")
            return TurnStatus.ERROR

        self.board[row][col] = player
        if self.check_win(row, col, player):
            return TurnStatus.WIN
        return TurnStatus.TURN

    def check_win(self, row, col, player) -> bool:
        # Проверяет горизонтальное направление
        if self.check_line(row, col, 0, 1, player) + self.check_line(row, col, 0, -1, player) >= self.NEED_TO_WIN - 1:
            return True

        # Проверяет вертикальное направление
        if self.check_line(row, col, 1, 0, player) + self.check_line(row, col, -1, 0, player) >= self.NEED_TO_WIN - 1:
            return True

        #  Проверяет диагональное направление (с левого-верхнего до правого-нижнего)
        if self.check_line(row, col, 1, 1, player) + self.check_line(row, col, -1, -1, player) >= self.NEED_TO_WIN - 1:
            return True

        # Проверяет диагональное направление (с левого-нижнего до правого-верхнего)
        if self.check_line(row, col, 1, -1, player) + self.check_line(row, col, -1, 1, player) >= self.NEED_TO_WIN - 1:
            return True

        return False

    def check_line(self, row, col, dr, dc, player):
        count = 0
        row, col = row + dr, col + dc
        while self.in_field(row, col) and self.board[row][col] == player:
            count += 1
            row += dr
            col += dc
        return count

    def in_field(self, row, col):
        return 0 <= row < self.ROW and 0 <= col < self.COL


if __name__ == "__main__":
    board = Board()

    board.add_move("G7", CellStatus.CROSS)
    board.add_move("H5", CellStatus.CIRCLE)
    board.add_move("A5", CellStatus.CROSS)
    board.add_move("O15", CellStatus.CIRCLE)
    board.add_move("A1", CellStatus.CROSS)
    board.add_move("A15", CellStatus.CIRCLE)
    board.add_move("O1", CellStatus.CROSS)

    board.add_move("!!", CellStatus.CIRCLE)

    print(board)
