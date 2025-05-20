from brain_games.scripts.game_manager import GameManager
from brain_games.games.prime_game import play_game

def main():
    manager = GameManager()
    manager.start_game(play_game)

if __name__ == "__main__":
    main()
   