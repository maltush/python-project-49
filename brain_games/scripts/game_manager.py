class GameManager:
    def __init__(self):
        self.max_rounds = 3

    def start_game(self, play_game):
        name = input("May I have your name? ")
        print(f"Hello, {name}!")

        success, correct_answer = play_game()
        
        if not success:
            print(f"'{correct_answer}' is the correct answer.")
            print(f"Let's try again, {name}!")
        else:
            print(f"Congratulations, {name}!")