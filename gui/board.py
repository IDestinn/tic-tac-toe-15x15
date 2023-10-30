from enum import Enum


class CellStatus(Enum):
    EMPTY = " "
    CROSS = "X"
    CIRCLE = "O"


class Board:

    def __init__(self, row: int = 15, col: int = 15, need_to_win: int = 5) -> None:
        self.row = row
        self.col = col
        self.need_to_win = need_to_win
        self.board = [[CellStatus.EMPTY for _ in range(self.col)] for _ in range(self.row)]
        self.game_result = None

    def __str__(self) -> str:
        board_str = "\n  ┌" + "───┬" * (self.col - 1) + "───┐\n"

        for i in range(self.row):
            num_of_row = self.row - i
            row = str(num_of_row) + "│" if num_of_row >= 10 else " " + str(num_of_row) + "│"

            for j in range(self.col):
                row += " " + self.board[i][j].value + " │"
            board_str += row + "\n"

            if i < self.row - 1:
                board_str += "  ├" + "───┼" * (self.col - 1) + "───┤\n"

        board_str += "  └" + "───┴" * (self.col - 1) + "───┘\n"
        board_str += "    " + "   ".join(chr(ord('A') + i) for i in range(self.col))

        return board_str

    def get_valid_moves(self) -> [(int, int)]:
        return [(i, j) for i, inner_array in enumerate(self.board)
                for j, element in enumerate(inner_array) if element == CellStatus.EMPTY]

    def convert_coord_to_index(self, player_input: str) -> [int, int]:
        col = int(ord(player_input[0].upper()) - ord('A'))
        row = self.row - int(player_input[1:])
        return row, col

    def convert_index_to_coord(self, row: int, col: int) -> str | None:
        if 0 <= row < self.row and 0 <= col < self.col:
            return chr(ord('A') + col) + str(self.row - row)
        return None

    def add_player_move(self, player_input: str, player: CellStatus) -> bool:
        if not 2 <= len(player_input) <= 3:
            print("Координаты записаны неверно")
            return False

        col_str = player_input[0]
        row_str = player_input[1:]

        if not 'A' <= col_str.upper() <= chr(ord('A') + self.col - 1):
            print("Координаты записаны неверно")
            return False

        try:
            row = int(row_str)
            if not 1 <= row <= self.row:
                print("Координаты записаны неверно")
                return False
        except ValueError:
            print("Координаты записаны неверно")
            return False

        row, col = self.convert_coord_to_index(player_input)

        if player not in CellStatus:
            print("Ошибка с определением символа")
            return False

        if self.board[row][col] != CellStatus.EMPTY:
            print("Клетка уже занята")
            return False

        self.board[row][col] = player
        return True

    def add_ai_move(self, player: CellStatus):
        from calc import calculate_best_move
        best_move = calculate_best_move(self, player)
        self.board[best_move[0]][best_move[1]] = player
        return best_move

    def add_move(self, row: int, col: int, player: CellStatus) -> None:
        self.board[row][col] = player
        self.check_win(row, col, player)

    def remove_move(self, row: int, col: int) -> None:
        self.board[row][col] = CellStatus.EMPTY
        self.game_result = None

    def check_win(self, row: int, col: int, player: CellStatus) -> bool:
        # Проверяет горизонтальное направление
        if self.check_line(row, col, 0, 1, player) + self.check_line(row, col, 0, -1, player) >= self.need_to_win - 1:
            self.game_result = player
            return True

        # Проверяет вертикальное направление
        if self.check_line(row, col, 1, 0, player) + self.check_line(row, col, -1, 0, player) >= self.need_to_win - 1:
            self.game_result = player
            return True

        #  Проверяет диагональное направление (с левого-верхнего до правого-нижнего)
        if self.check_line(row, col, 1, 1, player) + self.check_line(row, col, -1, -1, player) >= self.need_to_win - 1:
            self.game_result = player
            return True

        # Проверяет диагональное направление (с левого-нижнего до правого-верхнего)
        if self.check_line(row, col, 1, -1, player) + self.check_line(row, col, -1, 1, player) >= self.need_to_win - 1:
            self.game_result = player
            return True

        return False

    def check_line(self, row: int, col: int, row_directory: int, column_directory: int, player: CellStatus) -> int:
        count = 0
        row, col = row + row_directory, col + column_directory
        while 0 <= row < self.row and 0 <= col < self.col and self.board[row][col] == player:
            count += 1
            row += row_directory
            col += column_directory
        return count

    def in_field(self, row: int, col: int) -> bool:
        return 0 <= row < self.row and 0 <= col < self.col


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
