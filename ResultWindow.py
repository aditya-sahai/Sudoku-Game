import pygame
from PygameConfig import PygameConfig

class ResultWindow:
    def __init__(self, game_data, settings):
        self.MINUTES = game_data["mins"]
        self.SECONDS = game_data["secs"]
        self.DIFFICULTY = game_data["difficulty"]
        self.COMPUTER_SOLVED = game_data["computer-solved"]

        self.settings = settings

        self.loop_running = True

    def event_loop(self):
        """This event loop checks for the mouse hovers and clicks on the intro window."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.loop_running = False

    def draw_window(self):
        """Draws the window."""

        self.settings.win.fill(self.settings.BACKGROUND_COLOR)

        time_statement_text = self.settings.write_center_text(
            "Time Taken",
            pygame.Rect(0, 0 + self.settings.BLOCK_SIZE, self.settings.WIDTH, self.settings.HEIGHT // 4),
            (0, 0, 0),
            self.settings.GAME_STATS_FONT
        )

        time_digit_text = self.settings.write_center_text(
            f"{self.MINUTES} : {self.SECONDS}",
            pygame.Rect(0, self.settings.HEIGHT // 6 + self.settings.BLOCK_SIZE, self.settings.WIDTH, (self.settings.HEIGHT - self.settings.BLOCK_SIZE) // 4),
            (0, 0, 0),
            self.settings.GAME_STATS_FONT
        )

        difficulty_statement_text = self.settings.write_center_text(
            "Difficulty",
            pygame.Rect(0, self.settings.HEIGHT // 2 - self.settings.BLOCK_SIZE, self.settings.WIDTH, (self.settings.HEIGHT - self.settings.BLOCK_SIZE) // 3),
            (0, 0, 0),
            self.settings.GAME_STATS_FONT
        )

        difficulty_text = self.settings.write_center_text(
            self.DIFFICULTY,
            pygame.Rect(0, 2 * (self.settings.HEIGHT // 3) - self.settings.BLOCK_SIZE, self.settings.WIDTH, (self.settings.HEIGHT - self.settings.BLOCK_SIZE) // 3),
            (0, 0, 0),
            self.settings.GAME_STATS_FONT
        )

        note_text = self.settings.write_center_text(
            "Press Enter/Return To Proceed",
            self.settings.NOTE_RECT,
            (0, 0, 0),
            self.settings.NOTE_FONT
        )

        self.settings.win.blit(time_statement_text["text"], time_statement_text["rect"])
        self.settings.win.blit(time_digit_text["text"], time_digit_text["rect"])

        self.settings.win.blit(difficulty_statement_text["text"], difficulty_statement_text["rect"])
        self.settings.win.blit(difficulty_text["text"], difficulty_text["rect"])

        self.settings.win.blit(note_text["text"], note_text["rect"])

    def main(self):
        """Main loop of result."""

        while self.loop_running:
            self.event_loop()

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)


if __name__ == "__main__":
    settings = PygameConfig()
    FinalWindow = ResultWindow(settings, {'computer-solved': True, 'difficulty': 'medium', 'secs': '03', 'mins': '00'})
    FinalWindow.main()
