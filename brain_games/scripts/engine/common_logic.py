import random

def generate_random_numbers(min_value=1, max_value=100):
    return random.randint(min_value, max_value), random.randint(min_value, max_value)

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def format_question(num1, num2):
    return f"Question: {num1} {num2}"

def print_congratulations(name):
    print(f"Congratulations, {name}!")

def print_incorrect_answer(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
