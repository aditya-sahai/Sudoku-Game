import pygame
from PygameConfig import PygameConfig
from SudokuGenerator import SudokuGenerator
settings = PygameConfig()


class GameWindow:
    def __init__(self, difficulty, settings):
        self.settings = settings
        self.loop_running = True
        self.sudoku_surface = pygame.Surface((self.settings.SUDOKU_WIDTH, self.settings.SUDOKU_HEIGHT))
        self.SudokuGenerator = SudokuGenerator()
        self.SudokuGenerator.generate_board()
        self.SudokuGenerator.remove_values(difficulty)
        self.get_grid_dict()
        self.selected_box = self.SudokuGenerator.grid[4][4]

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

                self.SudokuGenerator.grid[row_num][col_num] = {
                    "value": self.SudokuGenerator.grid[row_num][col_num],
                    "can-change": self.SudokuGenerator.grid[row_num][col_num] == 0,
                    "rect": pygame.Rect(x, y, width, height),
                    "color": (0, 0, 0),
                }

    def make_sudoku_mouse_responsive(self):
        """Changes the color of the border if the mouse hovers on a rect."""

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0] - self.settings.SUDOKU_X
        mouse_y = mouse_pos[1] - self.settings.SUDOKU_Y

        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):
                if num_dict["rect"].collidepoint(mouse_x, mouse_y):
                    self.SudokuGenerator.grid[row_num][col_num]["color"] = (0, 0, 255)

                    if pygame.mouse.get_pressed()[0] == 1:
                        self.selected_box = self.SudokuGenerator.grid[row_num][col_num]
                    
                else:
                    self.SudokuGenerator.grid[row_num][col_num]["color"] = (0, 0, 0)

    def draw_sudoku(self):
        """Draws the sudoku surface."""

        self.sudoku_surface.fill((0, 0, 0))
        
        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):

                pygame.draw.rect(self.sudoku_surface, (255, 255, 255), num_dict["rect"])
                pygame.draw.rect(self.sudoku_surface, num_dict["color"], num_dict["rect"], 1)
                text = self.settings.write_center_text(num_dict["value"], num_dict["rect"], (0, 0, 0))

                if num_dict["value"] != 0:
                    self.sudoku_surface.blit(text["text"], text["rect"])
        
        pygame.draw.rect(self.sudoku_surface, (0, 0, 255), self.selected_box["rect"], 3)

    def draw_window(self):
        """Draws the game window."""

        self.settings.win.fill(self.settings.BACKGROUND_COLOR)
        
        self.draw_sudoku()
        self.settings.win.blit(self.sudoku_surface, (self.settings.SUDOKU_X, self.settings.SUDOKU_Y))

    def event_loop(self):
        """The event loop for events like closing he window."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop_running = False

    def main(self):
        """Main loop of the lobby window."""

        while self.loop_running:

            self.event_loop()
            self.make_sudoku_mouse_responsive()

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)


if __name__ == "__main__":
    # Game = GameWindow("easy")
    # # Game.main()

    Game = GameWindow("medium", settings)
    Game.main()

    # Game = GameWindow("hard")
    # Game.main()