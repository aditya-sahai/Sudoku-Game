import pygame


pygame.init()

class PygameConfig:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 700
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sudoku Masters")
        
        self.FPS = 30
        self.clock = pygame.time.Clock()

        self.BLOCK_SIZE = 50
        self.SUDOKU_WIDTH = 454
        self.SUDOKU_HEIGHT = 454
        self.SUDOKU_X = self.BLOCK_SIZE
        self.SUDOKU_Y = self.HEIGHT - self.BLOCK_SIZE - self.SUDOKU_HEIGHT

        self.BACKGROUND_COLOR = (200, 200, 200)
        # self.SUDOKU_NUMBER_FONT = pygame.font.SysFont("comicsansms", 36)
        self.SUDOKU_NUMBER_FONT = pygame.font.Font("Fonts/Howkins.ttf", 50)

        self.BOX_LINES_THICKNESS = 2

        self.GAME_WINDOW_HEADING_X = self.BLOCK_SIZE
        self.GAME_WINDOW_HEADING_Y = self.BLOCK_SIZE
        self.GAME_WINDOW_HEADING_WIDTH = self.SUDOKU_WIDTH * 1.5
        self.GAME_WINDOW_HEADING_HEIGHT = self.SUDOKU_Y - self.GAME_WINDOW_HEADING_Y - self.BLOCK_SIZE
        self.GAME_WINDOW_HEADING_RECT = pygame.Rect(
             self.GAME_WINDOW_HEADING_X,
             self.GAME_WINDOW_HEADING_Y,
             self.GAME_WINDOW_HEADING_WIDTH,
             self.GAME_WINDOW_HEADING_HEIGHT
        )

        self.HEADNG_FONT = pygame.font.Font("Fonts/Brianne.ttf", 150)
        self.HEADNG_FONT.set_underline(True)

        self.TIME_BOX_X = self.SUDOKU_X + self.SUDOKU_WIDTH + self.BLOCK_SIZE
        self.TIME_BOX_Y = self.SUDOKU_Y
        self.IME_BOX_WIDTH = self.BLOCK_SIZE * 4
        self.TIME_BOX_HEIGHT = self.BLOCK_SIZE * 3
        self.TIME_BOX_RECT = pygame.Rect(
            self.TIME_BOX_X,
            self.TIME_BOX_Y,
            self.IME_BOX_WIDTH,
            self.TIME_BOX_HEIGHT
        )
        self.TIME_BOX_COLOR = (100, 100, 100)

        self.SOLVE_BOX_X = self.SUDOKU_X + self.SUDOKU_WIDTH + self.BLOCK_SIZE
        self.SOLVE_BOX_Y = self.TIME_BOX_Y + self.TIME_BOX_HEIGHT + self.BLOCK_SIZE
        self.SOLVE_BOX_WIDTH = self.BLOCK_SIZE * 4
        self.SOLVE_BOX_HEIGHT = self.BLOCK_SIZE
        self.SOLVE_BOX_RECT = pygame.Rect(
            self.SOLVE_BOX_X,
            self.SOLVE_BOX_Y,
            self.SOLVE_BOX_WIDTH,
            self.SOLVE_BOX_HEIGHT
        )
        self.SOLVE_BOX_COLOR = (75, 255, 75)

        self.CHECK_BOX_X = self.SUDOKU_X + self.SUDOKU_WIDTH + self.BLOCK_SIZE
        self.CHECK_BOX_Y = self.SOLVE_BOX_Y + self.SOLVE_BOX_HEIGHT + self.BLOCK_SIZE
        self.CHECK_BOX_WIDTH = self.BLOCK_SIZE * 4
        self.CHECK_BOX_HEIGHT = self.BLOCK_SIZE
        self.CHECK_BOX_RECT = pygame.Rect(
            self.CHECK_BOX_X,
            self.CHECK_BOX_Y,
            self.CHECK_BOX_WIDTH,
            self.CHECK_BOX_HEIGHT
        )
        self.CHECK_BOX_COLOR = (75, 255, 75)

        self.SUBMIT_BOX_X = self.SUDOKU_X + self.SUDOKU_WIDTH + self.BLOCK_SIZE
        self.SUBMIT_BOX_Y = self.CHECK_BOX_Y + self.CHECK_BOX_HEIGHT + self.BLOCK_SIZE
        self.SUBMIT_BOX_WIDTH = self.BLOCK_SIZE * 4
        self.SUBMIT_BOX_HEIGHT = self.BLOCK_SIZE
        self.SUBMIT_BOX_RECT = pygame.Rect(
            self.SUBMIT_BOX_X,
            self.SUBMIT_BOX_Y,
            self.SUBMIT_BOX_WIDTH,
            self.SUBMIT_BOX_HEIGHT
        )
        self.SUBMIT_BOX_COLOR = (75, 255, 75)

        self.BUTTON_FONT = pygame.font.Font("Fonts/Howkins.ttf", 50)
    
    def write_center_text(self, text, rect, color, font):
        """Writes the given text at the center of the given rect"""

        rendered_text = font.render(str(text).strip(), True, color)
        text_rect = rendered_text.get_rect()
        text_rect.center = rect.center

        return {
            "text": rendered_text,
            "rect": text_rect,
        }


if __name__ == "__main__":
    Config = PygameConfig()
    