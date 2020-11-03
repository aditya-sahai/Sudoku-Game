import pygame
from PygameConfig import PygameConfig
from SudokuGenerator import SudokuGenerator
from Solver import Solver
import time


class GameWindow:
    def __init__(self, difficulty, settings):
        self.settings = settings

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

        if rect == self.settings.TIME_BOX_RECT:
            pygame.draw.rect(
                self.settings.win,
                (250, 250, 250),
                (self.settings.TIME_BOX_RECT.x + 2, self.settings.TIME_BOX_RECT.y + 2, self.settings.TIME_BOX_RECT.width - 4, self.settings.TIME_BOX_RECT.height - 4)
            )

        box_text = self.settings.write_center_text(
            str(text).strip(),
            rect,
            (0, 0, 0),
            self.settings.BUTTON_FONT
        )
        self.settings.win.blit(box_text["text"], box_text["rect"])
    
    def make_buttons_responsive(self, rect):
        """Change the color pf the buttons when hovered over and makes them functional."""

        mouse_pos = pygame.mouse.get_pos()
        mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
        color = (75, 255, 75)
        is_hovering = False

        if rect.collidepoint(mouse_pos):
            color = (255, 0, 0)
            is_hovering = True
        
        return {
            "is-pressed": mouse_is_pressed and not self.is_solving and is_hovering,
            "color": color,
        }

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
        
        self.draw_utility_box(self.settings.TIME_BOX_RECT, self.settings.TIME_BOX_COLOR, "Time")
        self.draw_utility_box(self.settings.SOLVE_BOX_RECT, self.settings.SOLVE_BOX_COLOR, "Solve")
        self.draw_utility_box(self.settings.CHECK_BOX_RECT, self.settings.CHECK_BOX_COLOR, "Check Box")
        self.draw_utility_box(self.settings.SUBMIT_BOX_RECT, self.settings.SUBMIT_BOX_COLOR, "Submit")

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

    def update_grid(self):
        """Updates the grid when the user enters a number."""

        if self.pressed_key != None:
            if self.SudokuGenerator.grid[self.selected_row][self.selected_col]["can-change"]:
                self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"] = self.pressed_key
    
    def solve(self):
        """Solves the board."""

        solve_mouse_status = self.make_buttons_responsive(self.settings.SOLVE_BOX_RECT)
        check_box_mouse_status = self.make_buttons_responsive(self.settings.CHECK_BOX_RECT)
        submit_mouse_status = self.make_buttons_responsive(self.settings.SUBMIT_BOX_RECT)

        self.settings.SOLVE_BOX_COLOR = solve_mouse_status["color"]
        self.settings.CHECK_BOX_COLOR = check_box_mouse_status["color"]
        self.settings.SUBMIT_BOX_COLOR = submit_mouse_status["color"]

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
                return (pos[0], col_num)

        # Checks if a number exists in the same column.
        for row in range(9):
            if num == self.SudokuGenerator.grid[row][pos[1]]["value"] and row != self.selected_row:
                return (row, pos[1])

        # Checks if number exists in the 3x3 box of number.
        box_x_start = (pos[0] // 3) * 3
        box_y_start = (pos[1] // 3) * 3

        for row_num, row in enumerate(self.SudokuGenerator.grid[box_x_start : box_x_start + 3]):
            for col_num, col in enumerate(row[box_y_start : box_y_start + 3]):
                if num == col["value"] and (self.SudokuGenerator.grid.index(row), row.index(col)) != (self.selected_row, self.selected_col):
                    return (self.SudokuGenerator.grid.index(row), row.index(col))

        return False
    
    def restore_grid(self):
        """Restores the grid."""

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):
                if num_dict["can-change"]:
                    self.SudokuGenerator.grid[row_num][col_num]["value"] = 0

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
            
            solve_mouse_status = self.make_buttons_responsive(self.settings.SOLVE_BOX_RECT)
            check_box_mouse_status = self.make_buttons_responsive(self.settings.CHECK_BOX_RECT)
            submit_mouse_status = self.make_buttons_responsive(self.settings.SUBMIT_BOX_RECT)

            self.settings.SOLVE_BOX_COLOR = solve_mouse_status["color"]
            self.settings.CHECK_BOX_COLOR = check_box_mouse_status["color"]
            self.settings.SUBMIT_BOX_COLOR = submit_mouse_status["color"]

            self.is_solving = solve_mouse_status["is-pressed"]

            if self.is_solving and not self.is_solved:
                self.restore_grid()
                self.solve()
                self.is_solved = True
                self.is_solving = False
            
            if check_box_mouse_status["is-pressed"] and self.SudokuGenerator.grid[self.selected_row][self.selected_col]["can-change"] and self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"] != 0:
                # time.sleep(1)
                same_num_pos = self.check_num(
                    self.SudokuGenerator.grid[self.selected_row][self.selected_col]["value"],
                    (self.selected_row, self.selected_col)
                )

                if same_num_pos and same_num_pos != (self.selected_row, self.selected_col):
                    self.SudokuGenerator.grid[same_num_pos[0]][same_num_pos[1]]["bg-color"] = (255, 100, 100)
                    self.SudokuGenerator.grid[self.selected_row][self.selected_col]["bg-color"] = (255, 100, 100)

                else:
                    self.SudokuGenerator.grid[self.selected_row][self.selected_col]["bg-color"] = (100, 255, 100)
                
                self.initial_time_check_num = time.time()

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


if __name__ == "__main__":
    # Game = GameWindow("easy")
    # # Game.main()

    settings = PygameConfig()

    Game = GameWindow("medium", settings)
    Game.main()

    # Game = GameWindow("hard")
    # Game.main()