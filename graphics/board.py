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
        board_str = "╒"
        board_str += "═══╤" * self.COL
        board_str = board_str[:-1] + "╕\n"
        seperate = "╞" + "═══╪" * self.COL
        seperate = seperate[:-1] + "╡\n"
        for i in range(self.ROW):
            row = "│"
            for j in range(self.COL):
                row += " " + self.board[i][j].value + " │"
            board_str += row + "\n"
            board_str += seperate
        end = "╘"
        end += "═══╧" * self.COL
        end = end[:-1] + "╛"
        board_str = board_str[:-62] + end
        return board_str


if __name__ == "__main__":
    board = Board()

    # Set some cells to be CROSS or CIRCLE for testing
    board.board[5][5] = Cell.CROSS
    board.board[7][7] = Cell.CIRCLE

    print(board)
