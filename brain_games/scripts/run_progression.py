from engine.game_manager import GameManager
from games.progression_game import play_game


if __name__ == "__main__":
    manager = GameManager()
    manager.start_game(play_game)