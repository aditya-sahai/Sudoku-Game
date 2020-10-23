from random import randint
import numpy as np


class SudokuGenerator:
    def __init__(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.is_solved = False
    
    def find_empty(self):
        """Returns the position of the first empty place in the grid."""

        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return (row, col)
    
    def check_num(self, num, row, col):
        """Checks is the number is valid for a particular position."""

        # checks if the number is in the same row
        try:
            if num in self.grid[row]:
                return (row, self.grid[row].index(num))
        
        except IndexError:
            print("Row, Col:", (row, col))
            print(np.array(self.grid))
            exit()

        # checks if the number is in the same column
        for y in range(9):
            if num == self.grid[y][col]:
                return (y, col)

        # checks is the number is in the same box
        box_row_start = row // 3 * 3
        box_col_start = col // 3 * 3

        for grid_row in self.grid[box_row_start : box_row_start + 3]:
            grid_col = grid_row[box_col_start : box_col_start + 3]
            if num in grid_col:
                return (self.grid.index(grid_row), grid_row.index(num))

    def find_pos_value(self):
        """Assigns a value to the place where the first 0 occurs."""

        empty_pos = self.find_empty()

        if not empty_pos:
            self.is_solved = True
            return

        else:
            row, col = empty_pos

        random_num = randint(1, 9)
        same_num_pos = self.check_num(num=random_num, row=row, col=col)

        if not same_num_pos:
            self.grid[row][col] = random_num

        else:
            for num in range(1, 10):
                if not self.check_num(num=num, row=row, col=col):
                    self.grid[row][col] = num
                    break

            else:                
                row, col = same_num_pos
                for temp_row in range(row, 9):
                    while col < 9:
                        self.grid[row][col] = 0
                        col += 1
                    col = 0
            
    def generate_board(self):
        """Generates a sudoku board."""
        
        while not self.is_solved:
            self.find_pos_value()


if __name__ == "__main__":
    Generator = SudokuGenerator()
    Generator.generate_board()
    # print(np.array(Generator.grid))

