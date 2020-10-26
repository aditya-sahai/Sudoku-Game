import pygame


pygame.init()

class PygameConfig:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 700
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.FPS = 30
        self.clock = pygame.time.Clock()

        self.BLOCK_SIZE = 50
        self.SUDOKU_WIDTH = 454
        self.SUDOKU_HEIGHT = 454
        self.SUDOKU_X = self.BLOCK_SIZE
        self.SUDOKU_Y = self.HEIGHT - self.BLOCK_SIZE - self.SUDOKU_HEIGHT

        self.BACKGROUND_COLOR = (200, 200, 200)
        self.font = pygame.font.SysFont("comicsansms", 36)
    
    def write_center_text(self, text, rect):
        """Writes the given text at the center of the given rect"""

        rendered_text = self.font.render(str(text).strip(), True, (0, 0, 0))
        text_rect = rendered_text.get_rect()
        text_rect.center = rect.center

        return {
            "text": rendered_text,
            "rect": text_rect,
        }


if __name__ == "__main__":
    Config = PygameConfig()
    