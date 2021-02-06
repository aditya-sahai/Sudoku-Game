from LobbyWindow import LobbyWindow
from GameWindow import GameWindow
from ResultWindow import ResultWindow
from PygameConfig import PygameConfig


settings = PygameConfig()
while True:
    Lobby = LobbyWindow(settings)
    LOBBY_DATA = Lobby.main()

    Game = GameWindow(LOBBY_DATA, settings)
    GAME_DATA = Game.main()

    if not GAME_DATA["computer-solved"]:
        Result = ResultWindow(GAME_DATA, settings)
        Result.main()

pygame.quit()
exit()
