from brain_games.games.calc_game import play_game
from brain_games.scripts.game_manager import GameManager


def main():
    manager = GameManager()
    manager.start_game(play_game)


if __name__ == "__main__":
    main()