class Solver:
    def __init__(self, board):
        self.grid = board
        # self.get_grid_dict()
    
    def get_grid_dict(self):
        """Changes the 2D list to a 2D list containing dictionaries."""

        for row_num in range(9):
            for col_num in range(9):
                self.grid[row_num][col_num] = {
                    "value": self.grid[row_num][col_num],
                    "can-change": self.grid[row_num][col_num] == 0,
                }

    def check_num(self, num, pos):
        """Checks the box the row and the column if the number is valid."""

        # Checks if the number exists in the same row.
        for num_dict in self.grid[pos[0]]:
            if num_dict["value"] == num:
                return False

        # Checks if a number exists in the same column.
        for col in range(9):
            if num == self.grid[col][pos[1]]["value"]:
                return False

        # Checks if number exists in the 3x3 box of number.
        box_x_start = (pos[0] // 3) * 3
        box_y_start = (pos[1] // 3) * 3

        for row in self.grid[box_x_start : box_x_start + 3]:
            for col in row[box_y_start : box_y_start + 3]:
                if num == col["value"]:
                    return False

        return True

    def find_empty(self):
        """Returns the row, col of next empty space."""
        
        for row in range(9):
            for col in range(9):
                if self.grid[row][col]["value"] == 0:
                    return (row, col)
        
        return None

    def solve_board(self):
        """Solves the sudoku and returns a 2d solved board."""
        
        empty_pos = self.find_empty()
        
        if not empty_pos:
            return True
        
        else:
            row, col = empty_pos

        for num in range(1, 10):
            if self.check_num(num, empty_pos):
                self.grid[row][col]["value"] = num

                if self.solve_board():
                    return True

                self.grid[row][col]["value"] = 0

        return False


if __name__ == "__main__":
    
    SUDOKU_BOARD = [
        [0, 0, 9, 2, 1, 8, 0, 0, 0],
        [1, 7, 0, 0, 9, 6, 8, 0, 0],
        [0, 4, 0, 0, 5, 0, 0, 0, 6],
        [4, 5, 1, 0, 6, 0, 3, 7, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 9],
        [9, 0, 2, 3, 7, 0, 5, 0, 0],
        [6, 0, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 4, 9, 2, 5, 7],
        [0, 9, 4, 8, 0, 0, 0, 1, 3],
    ]
    
    SudokuSolver = Solver(SUDOKU_BOARD)
    SudokuSolver.solve_board()
    print(SudokuSolver.grid)
