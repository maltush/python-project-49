import random


# Проверяет является ли число простым 
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Игровое взаимодействие. Добывваем рандомное число, спрашиваем, 
# вниваем ответ с правильным
def play_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):  
        number = random.randint(1, 1000)
        correct_answer = 'yes' if is_prime(number) else 'no'
        print(f"Question: {number}")
        user_answer = input('Your answer: ').strip().lower()

        if user_answer != correct_answer:
            return False, correct_answer
        
        print("Correct!")

    return True, None