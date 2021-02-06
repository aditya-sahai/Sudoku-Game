import pygame


pygame.init()

class PygameConfig:
    def __init__(self):
        # ------------------------------------------------------- General Config
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
        self.BUTTON_HOVERING_COLOR = (255, 100, 100)
        self.BUTTON_CLICK_COLOR = (255, 75, 75)
        # --------------------------------------------- General Config Ends Here


        # --------------------------------------------------- Game Window Config
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
        self.TIME_FONT = pygame.font.Font("Fonts/CourierPrime.ttf", 27)

        self.CHANGABLE_BOX_BG_COLOR = (255, 255, 255)
        self.UNCHANGABLE_BOX_BG_COLOR = (235, 235, 235)
        # ----------------------------------------- Game Window Config Ends Here


        # -------------------------------------------------- Lobby Window Config
        self.LOBBY_WINDOW_HEADING_X = self.BLOCK_SIZE
        self.LOBBY_WINDOW_HEADING_Y = self.BLOCK_SIZE * 2
        self.LOBBY_WINDOW_HEADING_WIDTH = self.SUDOKU_WIDTH * 1.5
        self.LOBBY_WINDOW_HEADING_HEIGHT = self.SUDOKU_Y - self.GAME_WINDOW_HEADING_Y - self.BLOCK_SIZE
        self.LOBBY_WINDOW_HEADING_RECT = pygame.Rect(
             self.LOBBY_WINDOW_HEADING_X,
             self.LOBBY_WINDOW_HEADING_Y,
             self.LOBBY_WINDOW_HEADING_WIDTH,
             self.LOBBY_WINDOW_HEADING_HEIGHT
        )

        self.DIFFICULTY_BOX_X = self.LOBBY_WINDOW_HEADING_X + 2 * self.BLOCK_SIZE
        self.DIFFICULTY_BOX_Y = self.LOBBY_WINDOW_HEADING_Y + self.LOBBY_WINDOW_HEADING_HEIGHT + 1.5 * self.BLOCK_SIZE
        self.DIFFICULTY_BOX_WIDTH = self.LOBBY_WINDOW_HEADING_WIDTH - 4 * self.BLOCK_SIZE
        self.DIFFICULTY_BOX_HEIGHT = 2 * self.BLOCK_SIZE
        self.DIFFICULTY_BOX_RECT = pygame.Rect(
             self.DIFFICULTY_BOX_X,
             self.DIFFICULTY_BOX_Y,
             self.DIFFICULTY_BOX_WIDTH,
             self.DIFFICULTY_BOX_HEIGHT
        )

        self.PLAY_BOX_X = self.LOBBY_WINDOW_HEADING_X + 2 * self.BLOCK_SIZE
        self.PLAY_BOX_Y = self.DIFFICULTY_BOX_Y + self.DIFFICULTY_BOX_HEIGHT + 1.5 * self.BLOCK_SIZE
        self.PLAY_BOX_WIDTH = self.LOBBY_WINDOW_HEADING_WIDTH - 4 * self.BLOCK_SIZE
        self.PLAY_BOX_HEIGHT = 2 * self.BLOCK_SIZE
        self.PLAY_BOX_RECT = pygame.Rect(
             self.PLAY_BOX_X,
             self.PLAY_BOX_Y,
             self.PLAY_BOX_WIDTH,
             self.PLAY_BOX_HEIGHT
        )
        self.PLAY_BOX_COLOR = (255, 255, 75)

        self.TOGGLE_SHOW_SOLVE_BOX_X = self.PLAY_BOX_RECT.center[0] - 4 * self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BOX_Y = self.PLAY_BOX_Y + self.PLAY_BOX_HEIGHT + 1 * self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BOX_WIDTH = 6 * self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BOX_HEIGHT = self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BOX_RECT = pygame.Rect(
             self.TOGGLE_SHOW_SOLVE_BOX_X,
             self.TOGGLE_SHOW_SOLVE_BOX_Y,
             self.TOGGLE_SHOW_SOLVE_BOX_WIDTH,
             self.TOGGLE_SHOW_SOLVE_BOX_HEIGHT
        )

        self.TOGGLE_SHOW_SOLVE_BUTTON_X = int(self.TOGGLE_SHOW_SOLVE_BOX_X + self.TOGGLE_SHOW_SOLVE_BOX_WIDTH + 0.5 * self.BLOCK_SIZE)
        self.TOGGLE_SHOW_SOLVE_BUTTON_Y = self.PLAY_BOX_Y + self.PLAY_BOX_HEIGHT + 1 * self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BUTTON_WIDTH = self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BUTTON_HEIGHT = self.BLOCK_SIZE
        self.TOGGLE_SHOW_SOLVE_BUTTON_RECT = pygame.Rect(
             self.TOGGLE_SHOW_SOLVE_BUTTON_X,
             self.TOGGLE_SHOW_SOLVE_BUTTON_Y,
             self.TOGGLE_SHOW_SOLVE_BUTTON_WIDTH,
             self.TOGGLE_SHOW_SOLVE_BUTTON_HEIGHT
        )

        self.HELP_CIRCLE_X = self.BLOCK_SIZE
        self.HELP_CIRCLE_Y = self.HEIGHT - self.BLOCK_SIZE
        self.HELP_CIRCLE_RADIUS = int(self.BLOCK_SIZE * 0.75)
        self.HELP_CIRCLE_RECT = pygame.Rect(
             self.HELP_CIRCLE_X - self.HELP_CIRCLE_RADIUS,
             self.HELP_CIRCLE_Y - self.HELP_CIRCLE_RADIUS,
             self.HELP_CIRCLE_RADIUS * 2,
             self.HELP_CIRCLE_RADIUS * 2
        )

        self.LOBBY_WINDOW_BOXES_COLOR = (255, 255, 75)
        self.SHOW_SOLVE_BUTTON_COLOR = (75, 255, 75)
        self.SHOW_SOLVE_OFF_BUTTON_COLOR = (255, 75, 75)

        self.HELP_CIRCLE_COLOR = (125, 125, 255)
        self.HELP_HOVERING_CIRCLE_COLOR = (100, 100, 255)
        self.HELP_CLICK_CIRCLE_COLOR = (90, 90, 255)

        self.LOBBY_WINDOW_DIFFICULTY_CHANGE_ARROW = pygame.image.load("Images\\up-arrow.jpg")
        self.LOBBY_WINDOW_RIGHT_ARROW = pygame.transform.rotate(self.LOBBY_WINDOW_DIFFICULTY_CHANGE_ARROW, 270)
        self.LOBBY_WINDOW_LEFT_ARROW = pygame.transform.rotate(self.LOBBY_WINDOW_DIFFICULTY_CHANGE_ARROW, 90)

        self.SIZE_INCREASE_PERCENT = 5
        self.ENLARGED_LOBBY_WINDOW_RIGHT_ARROW = pygame.transform.rotozoom(self.LOBBY_WINDOW_RIGHT_ARROW, 0, 1 + self.SIZE_INCREASE_PERCENT / 100)
        self.ENLARGED_LOBBY_WINDOW_LEFT_ARROW = pygame.transform.rotozoom(self.LOBBY_WINDOW_LEFT_ARROW, 0, 1 + self.SIZE_INCREASE_PERCENT / 100)

        self.SIZE_DECREASE_PERCENT = 5
        self.REDUCED_LOBBY_WINDOW_RIGHT_ARROW = pygame.transform.rotozoom(self.LOBBY_WINDOW_RIGHT_ARROW, 0, 1 - self.SIZE_DECREASE_PERCENT / 100)
        self.REDUCED_LOBBY_WINDOW_LEFT_ARROW = pygame.transform.rotozoom(self.LOBBY_WINDOW_LEFT_ARROW, 0, 1 - self.SIZE_DECREASE_PERCENT / 100)

        self.ARROWS_Y = int(self.DIFFICULTY_BOX_Y + 0.5 * self.BLOCK_SIZE)
        self.LEFT_ARROW_X = int(self.DIFFICULTY_BOX_X + 0.5 * self.BLOCK_SIZE)
        self.RIGHT_ARROW_X = int(self.DIFFICULTY_BOX_X + self.DIFFICULTY_BOX_WIDTH - (self.BLOCK_SIZE + self.BLOCK_SIZE * 0.5))

        # print(f"Left Arrow: {self.LEFT_ARROW_X} {self.ARROWS_Y}")
        # print(f"Right Arrow: {self.RIGHT_ARROW_X} {self.ARROWS_Y}")

        self.LOBBY_WINDOW_FONT = pygame.font.Font("Fonts/Howkins.ttf", 75)
        self.TOGGLE_SHOW_SOLVE_FONT = pygame.font.Font("Fonts/Howkins.ttf", 50)
        # ---------------------------------------- Lobby Window Config Ends Here

        # ------------------------------------------------- Result Window Config
        self.NOTE_X = 0
        self.NOTE_Y = self.HEIGHT - self.BLOCK_SIZE
        self.NOTE_WIDTH = self.WIDTH
        self.NOTE_HEIGHT = self.BLOCK_SIZE
        self.NOTE_RECT = pygame.Rect(
             self.NOTE_X,
             self.NOTE_Y,
             self.NOTE_WIDTH,
             self.NOTE_HEIGHT
        )

        self.GAME_STATS_FONT = pygame.font.Font("Fonts/Howkins.ttf", 100)
        self.NOTE_FONT = pygame.font.Font("Fonts/Howkins.ttf", 35)
        # --------------------------------------- Result Window Config Ends Here

    def write_center_text(self, text, rect, color, font):
        """Writes the given text at the center of the given rect"""

        rendered_text = font.render(str(text).strip(), True, color)
        text_rect = rendered_text.get_rect()
        text_rect.center = rect.center

        return {
            "text": rendered_text,
            "rect": text_rect,
        }

    def make_buttons_responsive(self, rect, base_color):
        """Change the color pf the buttons when hovered over and makes them functional."""

        mouse_pos = pygame.mouse.get_pos()
        mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
        color = base_color
        is_hovering = False

        if rect.collidepoint(mouse_pos):
            color = self.BUTTON_HOVERING_COLOR
            is_hovering = True
            if mouse_is_pressed:
                color = self.BUTTON_CLICK_COLOR

        else:
            color = base_color

        return {
            "is-pressed": mouse_is_pressed and is_hovering,
            "hovering": is_hovering,
            "color": color,
        }


if __name__ == "__main__":
    Config = PygameConfig()
