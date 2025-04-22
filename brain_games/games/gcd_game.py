import random
import math

def find_gcd(a, b):
    return math.gcd(a, b)

def play_game():
    print('Find the greatest common divisor of given numbers.')

    for _ in range(3): 
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = input('Your answer: ')

        if int(user_answer) != correct_answer:
            return False, correct_answer
        
        print("Correct!")

    return True, None