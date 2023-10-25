class SudokuSolver:
    def __init__(self, board):
        self.board = [[int(num) for num in row] for row in board]

    def get_first_empty_square(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j

    def validate_number(self, num, i, j):
        if num in self.board[i]:
            return False

        if num in [row[j] for row in self.board]:
            return False

        n, m = i//3, j//3
        if num in sum([row[3*m:3*m+3] for row in self.board[3*n:3*n+3]], []):
            return False
        return True

    def solved(self):
        empty_square = self.get_first_empty_square()
        if empty_square is not None:
            i, j = empty_square
        else:
            return True

        for n in range(1, 10):
            if self.validate_number(n, i, j):
                self.board[i][j] = n

                if self.solved():
                    return True
                self.board[i][j] = 0
        return False


def main():
    with open("sudoku.txt", "r") as file:
        sudoku = [row.rstrip("\n") for row in file.readlines()]
    sudoku_solver = SudokuSolver(sudoku)
    sudoku_solver.solved()
    for row in sudoku_solver.board:
        print(row)


if __name__ == "__main__":
    main()
