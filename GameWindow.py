import pygame
from PygameConfig import PygameConfig
from SudokuGenerator import SudokuGenerator


class GameWindow:
    def __init__(self, difficulty):
        self.settings = PygameConfig()
        self.loop_running = True
        self.sudoku_surface = pygame.Surface((self.settings.SUDOKU_WIDTH, self.settings.SUDOKU_HEIGHT))
        self.SudokuGenerator = SudokuGenerator()
        self.SudokuGenerator.generate_board()
        self.SudokuGenerator.remove_values(difficulty)
        self.get_grid_dict()

    def get_grid_dict(self):
        """Gets a 2d list containing dicts instead of just numbers."""

        for row_num in range(9):
            for col_num in range(9):

                if col_num % 3 == 0 and col_num != 0:
                    x = col_num * self.settings.BLOCK_SIZE + 4

                else:
                    x = col_num * self.settings.BLOCK_SIZE + 2
                
                if row_num % 3 == 0 and row_num != 0:
                    y = row_num * self.settings.BLOCK_SIZE + 4
                
                else:
                    y = row_num * self.settings.BLOCK_SIZE + 2

                self.SudokuGenerator.grid[row_num][col_num] = {
                    "value": self.SudokuGenerator.grid[row_num][col_num],
                    "can-change": self.SudokuGenerator.grid[row_num][col_num] == 0,
                    "rect": pygame.Rect(x, y, self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE),
                    "color": (0, 0, 0),
                }

    def draw_sudoku(self):
        """Draws the sudoku surface."""

        self.sudoku_surface.fill((0, 0, 0))
        
        for row_num, row in enumerate(self.SudokuGenerator.grid):
            for col_num, num_dict in enumerate(row):

                pygame.draw.rect(self.sudoku_surface, (255, 255, 255), num_dict["rect"])
                pygame.draw.rect(self.sudoku_surface, num_dict["color"], num_dict["rect"], 1)


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

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)


if __name__ == "__main__":
    Game = GameWindow("easy")
    Game.main()