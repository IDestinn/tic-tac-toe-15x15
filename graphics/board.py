from enum import Enum

class Cell(Enum):
    EMPTY = " "
    CROSS = "X"
    CIRCLE = "O"

class Board():

    def __init__(self) -> None:
        self.ROW = 15
        self.COL = 15
        self.board = [[Cell.EMPTY for i in range(self.COL)] for j in range(self.ROW)]

    def __str__(self) -> str:
        board_str = "  ┌" + "───┬" * (self.COL - 1) + "───┐\n"

        for i in range(self.ROW):
            num_of_row = 15 - i
            row = str(num_of_row) + "│" if num_of_row >= 10 else " " + str(num_of_row) + "│"

            for j in range(self.COL):
                row += " " + self.board[i][j].value + " │"
            board_str += row + "\n"

            if i < self.ROW - 1:
                board_str += "  ├" + "───┼" * (self.COL - 1) + "───┤\n"

        board_str += "  └" + "───┴" * (self.COL - 1) + "───┘\n"
        board_str += "    " + "   ".join(chr(ord('A') + i) for i in range(self.COL))

        return board_str
    
    def add_move(self, input, player) -> int:
        try:
            col = int(ord(input[0]) - ord('A'))
            row = 15 - int(input[1:3])
        except ValueError:
            print("Координаты записаны неверно")
            return -1
        
        if not self.is_valid(row, col):
            print("Координаты записаны неверно")
            return -1
        
        if player not in Cell:
            print("Ошибка с определением символа")
            return -2
        
        if self.board[row][col] != Cell.EMPTY:
            print("Клетка уже занята")
            return -3
        
        self.board[row][col] = player
        return 0
    
    def check_win(self, row, col, player) -> bool:
        # Check for a win after a player's move at (row, col)

        # Check horizontally
        if self.check_line(row, col, 0, 1, player) + self.check_line(row, col, 0, -1, player) >= 4:
            return True

        # Check vertically
        if self.check_line(row, col, 1, 0, player) + self.check_line(row, col, -1, 0, player) >= 4:
            return True

        # Check diagonally (top-left to bottom-right)
        if self.check_line(row, col, 1, 1, player) + self.check_line(row, col, -1, -1, player) >= 4:
            return True

        # Check diagonally (bottom-left to top-right)
        if self.check_line(row, col, 1, -1, player) + self.check_line(row, col, -1, 1, player) >= 4:
            return True

        return False
    
    def check_line(self, row, col, dr, dc, player):
        # Helper function to check for a win in a specific direction (dr, dc)
        count = 0
        r, c = row, col
        while self.is_valid(r, c) and self.board[r][c] == player:
            count += 1
            r += dr
            c += dc
        return count

    def is_valid(self, row, col):
        return 0 <= row < self.ROW and 0 <= col < self.COL


if __name__ == "__main__":
    board = Board()

    board.add_move("G7", Cell.CROSS)
    board.add_move("H5", Cell.CIRCLE)
    board.add_move("A5", Cell.CROSS)
    board.add_move("O15", Cell.CIRCLE)
    board.add_move("A1", Cell.CROSS)
    board.add_move("A15", Cell.CIRCLE)
    board.add_move("O1", Cell.CROSS)

    board.add_move("!!", Cell.CIRCLE)

    print(board)
