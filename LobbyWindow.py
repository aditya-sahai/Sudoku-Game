import pygame
from PygameConfig import PygameConfig
settings = PygameConfig()


class LobbyWindow:
    def __init__(self, settings):
        self.loop_running = True
        self.settings = settings
        self.difficulties_list = ["easy", "medium", "hard"]
        self.selected_difficulty_num = 0

    def draw_window(self):
        """Draws the lobby window."""

        self.settings.win.fill(self.settings.BACKGROUND_COLOR)

        heading_text = self.settings.write_center_text(
            "Sudoku Masters",
            self.settings.LOBBY_WINDOW_HEADING_RECT,
            (0, 0, 0),
            self.settings.HEADNG_FONT
        )
        play_text = self.settings.write_center_text(
            "Play",
            self.settings.PLAY_BOX_RECT,
            (0, 0, 0),
            self.settings.LOBBY_WINDOW_FONT
        )

        difficulty_text = self.settings.write_center_text(
            self.difficulties_list[self.selected_difficulty_num],
            self.settings.DIFFICULTY_BOX_RECT,
            (0, 0, 0),
            self.settings.LOBBY_WINDOW_FONT
        )


        self.settings.win.blit(heading_text["text"], heading_text["rect"])

        pygame.draw.rect(self.settings.win, self.settings.LOBBY_WINDOW_BOXES_COLOR, self.settings.DIFFICULTY_BOX_RECT)
        pygame.draw.rect(self.settings.win, self.settings.LOBBY_WINDOW_BOXES_COLOR, self.settings.PLAY_BOX_RECT)

        self.settings.win.blit(play_text["text"], play_text["rect"])
        self.settings.win.blit(difficulty_text["text"], difficulty_text["rect"])

        self.settings.win.blit(self.settings.LOBBY_WINDOW_LEFT_ARROW, (self.settings.LEFT_ARROW_X, self.settings.ARROWS_Y))
        self.settings.win.blit(self.settings.LOBBY_WINDOW_RIGHT_ARROW, (self.settings.RIGHT_ARROW_X, self.settings.ARROWS_Y))

    def event_loop(self):
        """This event loop checks for the mouse hovers and clicks on the intro window."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def main(self):
        """Main loop of the lobby window."""

        while self.loop_running:

            self.event_loop()

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)


if __name__ == "__main__":
    Lobby = LobbyWindow(settings)
    Lobby.main()
