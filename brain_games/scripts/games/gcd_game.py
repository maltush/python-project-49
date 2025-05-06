import math
import random


# Вычисляет НОД 
def find_gcd(a, b):
    return math.gcd(a, b)


# Игровое взаимодействие. Добываем два рандомных числа, спрашиваем, сравниваем ответ с правильным
def play_game():
    print('Find the greatest common divisor of given numbers.')

    for _ in range(3): 
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = input('Your answer: ')

        if str(user_answer) != str(correct_answer):
            return False, correct_answer
        
        print("Correct!")

    return True, None 