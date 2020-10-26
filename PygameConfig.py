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


if __name__ == "__main__":
    Config = PygameConfig()
    