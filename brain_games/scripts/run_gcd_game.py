from games.gcd_game import play_game
from engine.game_manager import GameManager

if __name__ == "__main__":
    manager = GameManager()
    manager.start_game(play_game)
