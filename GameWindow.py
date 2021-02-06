import pygame
from PygameConfig import PygameConfig
from SudokuGenerator import SudokuGenerator
from Solver import Solver
import time


class GameWindow:
    def __init__(self, difficulty, settings):
        self.settings = settings
        self.DIFFICULTY = difficulty

        self.loop_running = True
        self.sudoku_surface = pygame.Surface((self.settings.SUDOKU_WIDTH, self.settings.SUDOKU_HEIGHT))

        self.SudokuGenerator = SudokuGenerator()
        self.SudokuGenerator.generate_board()
        self.SudokuGenerator.remove_values(difficulty)
        self.get_grid_dict()

        self.Solver = Solver(self.SudokuGenerator.grid)

        self.selected_row = 4
        self.selected_col = 4

        self.pressed_key = None

        self.is_solving = False
        self.is_solved = False
        self.initial_time_check_num = 0
        self.elapsed_time_check_box = 0

        self.sudoku_start_time = time.time()
        self.elapsed_time = 60 # round(time.time() - self.sudoku_start_time, 2)
        self.elapsed_minutes = int(self.elapsed_time // 60)
        self.elapsed_seconds = self.elapsed_time - (self.elapsed_minutes * 60)

    def get_grid_dict(self):
        """Gets a 2d list containing dicts instead of just numbers."""

        for row_num in range(9):
            height = self.settings.BLOCK_SIZE
            y = row_num * self.settings.BLOCK_SIZE + self.settings.BOX_LINES_THICKNESS

            if row_num % 3 == 0 and row_num != 0:
                y += self.settings.BOX_LINES_THICKNESS
                height -= self.settings.BOX_LINES_THICKNESS

            for col_num in range(9):
                width = self.settings.BLOCK_SIZE
                x = col_num * self.settings.BLOCK_SIZE + self.settings.BOX_LINES_THICKNESS

                if col_num % 3 == 0 and col_num != 0:
                    x += self.settings.BOX_LINES_THICKNESS
                    width -= self.settings.BOX_LINES_THICKNESS

                if self.SudokuGenerator.grid[row_num][col_num] == 0:
                    bg_color = self.settings.CHANGABLE_BOX_BG_COLOR

                else:
                    bg_color = self.settings.UNCHANGABLE_BOX_BG_COLOR

                self.SudokuGenerator.grid[row_num][col_num] = {
                    "value": self.SudokuGenerator.grid[row_num][col_num],
                    "can-change": self.SudokuGenerator.grid[row_num][col_num] == 0,
                    "rect": pygame.Rect(x, y, width, height),
                    "border-color": (0, 0, 0),
                    "bg-color": bg_color,
                }

    def make_sudoku_mouse_responsive(self):
        """Changes the color of the border if the mouse hovers on a rect."""

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0] - self.settings.SUDOKU_X
        mouse_y = mouse_pos[1] - self.settings.SUDOKU_Y

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):
                if num_dict["rect"].collidepoint(mouse_x, mouse_y):
                    self.SudokuGenerator.grid[row_num][col_num]["border-color"] = (0, 0, 255)

                    if pygame.mouse.get_pressed()[0] == 1:
                        self.selected_row = row_num
                        self.selected_col = col_num

                else:
                    self.SudokuGenerator.grid[row_num][col_num]["border-color"] = (0, 0, 0)

    def draw_sudoku(self):
        """Draws the sudoku surface."""

        self.sudoku_surface.fill((0, 0, 0))

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):

                pygame.draw.rect(self.sudoku_surface, num_dict["bg-color"], num_dict["rect"])
                pygame.draw.rect(self.sudoku_surface, num_dict["border-color"], num_dict["rect"], 1)
                text = self.settings.write_center_text(
                    num_dict["value"],
                    num_dict["rect"],
                    (0, 0, 0),
                    self.settings.SUDOKU_NUMBER_FONT
                )

                if num_dict["value"] != 0:
                    self.sudoku_surface.blit(text["text"], text["rect"])

        pygame.draw.rect(self.sudoku_surface, (0, 0, 255), self.SudokuGenerator.grid[self.selected_row][self.selected_col]["rect"], 3)

    def draw_utility_box(self, rect, color, text):
        """Draws the time button, solve button and check box button."""

        pygame.draw.rect(self.settings.win, color, rect)
        font = self.settings.BUTTON_FONT

        if rect == self.settings.TIME_BOX_RECT:
            font = self.settings.TIME_FONT
            pygame.draw.rect(
                self.settings.win,
                (250, 250, 250),
                (self.settings.TIME_BOX_RECT.x + 2, self.settings.TIME_BOX_RECT.y + 2, self.settings.TIME_BOX_RECT.width - 4, self.settings.TIME_BOX_RECT.height - 4)
            )

            rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height // 2)
            box_text = self.settings.write_center_text(
                f"Min: {str(self.elapsed_minutes).strip()}",
                rect,
                (0, 0, 0),
                font
            )
            self.settings.win.blit(box_text["text"], box_text["rect"])
            pygame.draw.line(self.settings.win, (0, 0, 0), (rect.x + 2, rect.y + rect.height), (rect.x + rect.width - 2, rect.y + rect.height))

            rect = pygame.Rect(rect.x, rect.y + rect.height, rect.width, rect.height)
            box_text = self.settings.write_center_text(
                f"Sec: {str(self.elapsed_seconds).strip()}",
                rect,
                (0, 0, 0),
                font
            )
            self.settings.win.blit(box_text["text"], box_text["rect"])

            return

        box_text = self.settings.write_center_text(
            str(text).strip(),
            rect,
            (0, 0, 0),
            font
        )

        self.settings.win.blit(box_text["text"], box_text["rect"])

    def draw_window(self):
        """Draws the game window."""

        self.settings.win.fill(self.settings.BACKGROUND_COLOR)

        self.draw_sudoku()
        self.settings.win.blit(self.sudoku_surface, (self.settings.SUDOKU_X, self.settings.SUDOKU_Y))

        text = self.settings.write_center_text(
            "Sudoku Masters",
            self.settings.GAME_WINDOW_HEADING_RECT,
            (0, 0, 0),
            self.settings.HEADNG_FONT
        )
        self.settings.win.blit(text["text"], text["rect"])

        self.draw_utility_box(self.settings.TIME_BOX_RECT, self.settings.TIME_BOX_COLOR, str(self.elapsed_time))
        self.draw_utility_box(self.settings.SOLVE_BOX_RECT, self.solve_box_color, "Solve")
        self.draw_utility_box(self.settings.CHECK_BOX_RECT, self.check_box_color, "Check Box")

        if not self.is_solved:
            submit_button_text = "Submit"

        else:
            submit_button_text = "Proceed"

        self.draw_utility_box(self.settings.SUBMIT_BOX_RECT, self.submit_box_color, submit_button_text)

    def event_loop(self):
        """The event loop for events like closing he window."""

        self.pressed_key = None

        for event in pygame.event.get():

            pressed = pygame.key.get_pressed()
            self.shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE:
                    self.pressed_key = 0
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    self.pressed_key = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    self.pressed_key = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    self.pressed_key = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    self.pressed_key = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    self.pressed_key = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    self.pressed_key = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    self.pressed_key = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    self.pressed_key = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    self.pressed_key = 9
                elif event.key == pygame.K_UP:
                    if self.selected_row == 0:
                        self.selected_row = 8
                    else:
                        self.selected_row -= 1
                elif event.key == pygame.K_DOWN:
                    if self.selected_row == 8:
                        self.selected_row = 0
                    else:
                        self.selected_row += 1
                elif event.key == pygame.K_LEFT:
                    if self.selected_col == 0:
                        self.selected_col = 8
                    else:
                        self.selected_col -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.selected_col == 8:
                        self.selected_col = 0
                    else:
                        self.selected_col += 1

    def update_grid(self):
        """Updates the grid when the user enters a number."""

        if self.pressed_key != None:
            if self.SudokuGenerator.grid[self.selected_row][self.selected_col]["can-change"]:
                self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"] = self.pressed_key

    def solve(self):
        """Solves the board."""

        solve_mouse_status = self.settings.make_buttons_responsive(self.settings.SOLVE_BOX_RECT, self.settings.SOLVE_BOX_COLOR)
        check_box_mouse_status = self.settings.make_buttons_responsive(self.settings.CHECK_BOX_RECT, self.settings.CHECK_BOX_COLOR)
        submit_mouse_status = self.settings.make_buttons_responsive(self.settings.SUBMIT_BOX_RECT, self.settings.SUBMIT_BOX_COLOR)

        self.solve_box_color = solve_mouse_status["color"]
        self.check_box_color = check_box_mouse_status["color"]
        self.submit_box_color = submit_mouse_status["color"]

        empty_pos = self.Solver.find_empty()
        self.event_loop()

        if not empty_pos:
            return True

        else:
            row, col = empty_pos

        for num in range(1, 10):
            if not self.Solver.check_num(num, empty_pos):
                self.SudokuGenerator.grid[row][col]["value"] = num
                self.selected_row = row
                self.selected_col = col

                self.draw_window()
                pygame.display.update()

                self.settings.clock.tick(self.settings.FPS * 4)

                if self.solve():
                    return True

                self.SudokuGenerator.grid[row][col]["value"] = 0

        return False

    def check_num(self, num, pos):
        """Checks the box the row and the column if the number is valid."""

        # Checks if the number exists in the same row.
        for col_num, num_dict in enumerate(self.SudokuGenerator.grid[pos[0]]):
            if num_dict["value"] == num and col_num != self.selected_col:
                # print("SAME ROW")
                return (pos[0], col_num)

        # Checks if a number exists in the same column.
        for row in range(9):
            if num == self.SudokuGenerator.grid[row][pos[1]]["value"] and row != self.selected_row:
                # print("SAME COL")
                return (row, pos[1])

        # Checks if number exists in the 3x3 box of number.
        box_x_start = (pos[0] // 3) * 3
        box_y_start = (pos[1] // 3) * 3

        for row_num, row in enumerate(self.SudokuGenerator.grid[box_x_start : box_x_start + 3]):
            for col_num, col in enumerate(row[box_y_start : box_y_start + 3]):
                if num == col["value"] and (self.SudokuGenerator.grid.index(row), row.index(col)) != (self.selected_row, self.selected_col):
                    # print("SAME BOX")
                    return (self.SudokuGenerator.grid.index(row), row.index(col))

        return False

    def check_submitted_sudoku(self):
        """Checks the sudoku. Is called on clicking submit button."""

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, col in enumerate(row):

                self.selected_row, self.selected_col = (row_num, col_num)

                if not self.check_box_change_colors():
                    return False

        return True

    def restore_grid(self):
        """Restores the grid."""

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):
                if num_dict["can-change"]:
                    self.SudokuGenerator.grid[row_num][col_num]["value"] = 0

    def check_box_change_colors(self):
        """Checks if the num at the selected row and col is valid and changes colors accordingly."""

        same_num_pos = self.check_num(
            self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"],
            (self.selected_row, self.selected_col)
        )

        if same_num_pos and self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"] != 0:
            self.SudokuGenerator.grid[same_num_pos[0]][same_num_pos[1]]["bg-color"] = (255, 100, 100)
            self.SudokuGenerator.grid[self.selected_row][self.selected_col]["bg-color"] = (255, 100, 100)
            is_valid = False

        elif self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"] == 0:
            self.SudokuGenerator.grid[self.selected_row][self.selected_col]["bg-color"] = (255, 100, 100)
            is_valid = False

        else:
            if self.is_solving:
                self.SudokuGenerator.grid[self.selected_row][self.selected_col]["bg-color"] = (100, 255, 100)
            is_valid = True

        self.initial_time_check_num = time.time()
        return is_valid

    def clear_check_box_colors(self):
        """Clears all the colors acquired by the check box button."""

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):
                if num_dict["can-change"]:
                    self.SudokuGenerator.grid[row_num][col_num]["bg-color"] = self.settings.CHANGABLE_BOX_BG_COLOR

                else:
                    self.SudokuGenerator.grid[row_num][col_num]["bg-color"] = self.settings.UNCHANGABLE_BOX_BG_COLOR

    def main(self):
        """Main loop of the lobby window."""

        while self.loop_running:

            self.event_loop()
            self.make_sudoku_mouse_responsive()

            if not self.is_solving and not self.is_solved:
                self.elapsed_time = round(time.time() - self.sudoku_start_time)
                self.elapsed_minutes = str(int(self.elapsed_time // 60))
                self.elapsed_minutes = f"{'0' * (2 - len(self.elapsed_minutes))}{self.elapsed_minutes}"

                self.elapsed_seconds = str(self.elapsed_time - (int(self.elapsed_minutes) * 60))
                self.elapsed_seconds = f"{'0' * (2 - len(self.elapsed_seconds))}{self.elapsed_seconds}"

            solve_mouse_status = self.settings.make_buttons_responsive(self.settings.SOLVE_BOX_RECT, self.settings.SOLVE_BOX_COLOR)
            check_box_mouse_status = self.settings.make_buttons_responsive(self.settings.CHECK_BOX_RECT, self.settings.CHECK_BOX_COLOR)
            submit_mouse_status = self.settings.make_buttons_responsive(self.settings.SUBMIT_BOX_RECT, self.settings.SUBMIT_BOX_COLOR)

            self.solve_box_color = solve_mouse_status["color"]
            self.check_box_color = check_box_mouse_status["color"]
            self.submit_box_color = submit_mouse_status["color"]

            self.is_solving = solve_mouse_status["is-pressed"]

            if self.is_solving and not self.is_solved:
                self.restore_grid()
                self.solve()
                self.is_solved = True
                self.computer_solved = True
                self.is_solving = False

            elif submit_mouse_status["is-pressed"] and self.is_solved:
                self.loop_running = False

            if check_box_mouse_status["is-pressed"] and self.SudokuGenerator.grid[self.selected_row][self.selected_col]["can-change"]:
                self.check_box_change_colors()

            if submit_mouse_status["is-pressed"] and not self.is_solved:
                solved_status = self.check_submitted_sudoku()
                if solved_status:
                    self.computer_solved = False

            if not self.is_solved:
                self.update_grid()

            if self.initial_time_check_num != 0:
                self.elapsed_time_check_box = time.time() - self.initial_time_check_num

            if self.elapsed_time_check_box >= 5:
                self.clear_check_box_colors()
                self.initial_time_check_num = 0
                self.elapsed_time_check_box = 0


            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)

        return {
            "computer-solved": self.computer_solved,
            "difficulty": self.DIFFICULTY,
            "secs": self.elapsed_seconds,
            "mins": self.elapsed_minutes,
        }

if __name__ == "__main__":
    settings = PygameConfig()

    Game = GameWindow("medium", settings)
    game_data = Game.main()
    pygame.quit()
    print(game_data)
