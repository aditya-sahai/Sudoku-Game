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
        self.GAME_WINDOW_HEADING_WIDTH = 1.5 * self.SUDOKU_WIDTH
        self.GAME_WINDOW_HEADING_HEIGHT = self.SUDOKU_Y - self.GAME_WINDOW_HEADING_Y - self.BLOCK_SIZE
        self.GAME_WINDOW_HAEDING_RECT = pygame.Rect(
             self.GAME_WINDOW_HEADING_X,
             self.GAME_WINDOW_HEADING_Y,
             self.GAME_WINDOW_HEADING_WIDTH,
             self.GAME_WINDOW_HEADING_HEIGHT
        )

        self.HEADNG_FONT = pygame.font.Font("Fonts/Brianne.ttf", 150)
        self.HEADNG_FONT.set_underline(True)
    
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
    