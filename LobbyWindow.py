import pygame
from math import hypot
from PygameConfig import PygameConfig


class LobbyWindow:
    def __init__(self, settings):
        self.loop_running = True
        self.settings = settings
        self.difficulties_list = ["easy", "medium", "hard"]
        self.selected_difficulty_num = 0

        self.play_box_color = self.settings.PLAY_BOX_COLOR
        self.toggle_box_color = self.settings.SHOW_SOLVE_BUTTON_COLOR
        self.help_circle_color = self.settings.HELP_CIRCLE_COLOR

        self.show_solve_counter = 0
        self.left_arrow_counter = 0
        self.right_arrow_counter = 0

    def check_mouse_help_circle_overlap(self):
        """Checks if the mouse is colliding with the circle."""

        mouse_pos = pygame.mouse.get_pos()
        mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
        is_hovering = False

        dist_x = mouse_pos[0] - self.settings.HELP_CIRCLE_RECT.centerx
        dist_y = mouse_pos[1] - self.settings.HELP_CIRCLE_RECT.centery

        if hypot(dist_x, dist_y) < self.settings.HELP_CIRCLE_RADIUS:
            self.help_circle_color = self.settings.HELP_HOVERING_CIRCLE_COLOR
            if mouse_is_pressed:
                self.help_circle_color = self.settings.HELP_CLICK_CIRCLE_COLOR
                is_hovering = True
        else:
            self.help_circle_color = self.settings.HELP_CIRCLE_COLOR

        return {
            "is-pressed": mouse_is_pressed and is_hovering
        }

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

        toggle_show_solve_text = self.settings.write_center_text(
            "Toggle Show Solve",
            self.settings.TOGGLE_SHOW_SOLVE_BOX_RECT,
            (0, 0, 0),
            self.settings.TOGGLE_SHOW_SOLVE_FONT
        )

        help_circle_text = self.settings.write_center_text(
            "?",
            self.settings.HELP_CIRCLE_RECT,
            (0, 0, 0),
            self.settings.TOGGLE_SHOW_SOLVE_FONT
        )

        self.settings.win.blit(heading_text["text"], heading_text["rect"])

        pygame.draw.rect(self.settings.win, self.settings.LOBBY_WINDOW_BOXES_COLOR, self.settings.DIFFICULTY_BOX_RECT)
        pygame.draw.rect(self.settings.win, self.play_box_color, self.settings.PLAY_BOX_RECT)

        self.settings.win.blit(play_text["text"], play_text["rect"])
        self.settings.win.blit(difficulty_text["text"], difficulty_text["rect"])

        self.settings.win.blit(self.settings.LOBBY_WINDOW_LEFT_ARROW, (self.settings.LEFT_ARROW_X, self.settings.ARROWS_Y))
        self.settings.win.blit(self.settings.LOBBY_WINDOW_RIGHT_ARROW, (self.settings.RIGHT_ARROW_X, self.settings.ARROWS_Y))

        self.settings.win.blit(toggle_show_solve_text["text"], toggle_show_solve_text["rect"])
        pygame.draw.rect(self.settings.win, self.toggle_box_color, self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT)
        pygame.draw.rect(self.settings.win, (0, 0, 0), (self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT.x - 1, self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT.y - 1, self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT.width + 2, self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT.height + 2), 1)

        pygame.draw.circle(self.settings.win, self.help_circle_color, (self.settings.HELP_CIRCLE_X, self.settings.HELP_CIRCLE_Y), self.settings.HELP_CIRCLE_RADIUS)
        self.settings.win.blit(help_circle_text["text"], help_circle_text["rect"])

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
            help_circle_status = self.check_mouse_help_circle_overlap()

            play_mouse_status = self.settings.make_buttons_responsive(self.settings.PLAY_BOX_RECT, self.settings.PLAY_BOX_COLOR)
            toggle_mouse_status = self.settings.make_buttons_responsive(self.settings.TOGGLE_SHOW_SOLVE_BUTTON_RECT, self.settings.SHOW_SOLVE_BUTTON_COLOR)
            left_arrow_mouse_status = self.settings.make_buttons_responsive(pygame.Rect(self.settings.LEFT_ARROW_X, self.settings.ARROWS_Y, self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE), None)
            right_arrow_mouse_status = self.settings.make_buttons_responsive(pygame.Rect(self.settings.RIGHT_ARROW_X, self.settings.ARROWS_Y, self.settings.BLOCK_SIZE, self.settings.BLOCK_SIZE), None)

            self.play_box_color = play_mouse_status["color"]

            if left_arrow_mouse_status["is-pressed"] and self.left_arrow_counter >= 4:
                if self.selected_difficulty_num != 0:
                    self.selected_difficulty_num -= 1
                    self.left_arrow_counter = 0

            elif right_arrow_mouse_status["is-pressed"] and self.right_arrow_counter >= 4:
                if self.selected_difficulty_num != 2:
                    self.selected_difficulty_num += 1
                    self.right_arrow_counter = 0

            if toggle_mouse_status["is-pressed"]:
                if self.toggle_box_color == self.settings.SHOW_SOLVE_BUTTON_COLOR and self.show_solve_counter >= 4:
                    self.toggle_box_color = self.settings.SHOW_SOLVE_OFF_BUTTON_COLOR
                    self.show_solve_counter = 0
                elif self.toggle_box_color == self.settings.SHOW_SOLVE_OFF_BUTTON_COLOR and self.show_solve_counter >= 4:
                    self.toggle_box_color = self.settings.SHOW_SOLVE_BUTTON_COLOR
                    self.show_solve_counter = 0

            if play_mouse_status["is-pressed"]:
                self.loop_running = False
                show_solve = self.toggle_box_color == self.settings.SHOW_SOLVE_BUTTON_COLOR

            if help_circle_status["is-pressed"]:
                self.loop_running = False
                show_solve = self.toggle_box_color == self.settings.SHOW_SOLVE_BUTTON_COLOR

            self.show_solve_counter += 1
            self.left_arrow_counter += 1
            self.right_arrow_counter += 1

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)

        return {
            "difficulty": self.difficulties_list[self.selected_difficulty_num],
            "show-solve": show_solve,
        }

if __name__ == "__main__":
    settings = PygameConfig()

    Lobby = LobbyWindow(settings)
    lobby_data = Lobby.main()
    pygame.quit()
    print(lobby_data)