import random


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    score = 0
    rounds = 3

    for _ in range(rounds):
        number = random.randint(1, 100)
        correct_answer = 'yes' if is_even(number) else 'no'
        
        print(f"Question: {number}")
        user_answer = input('Your answer: ').strip().lower()

        if user_answer != correct_answer:
            print(
            f"'{user_answer}' is wrong answer ;(. ",
            f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return 
        
        print("Correct!")
        score += 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()