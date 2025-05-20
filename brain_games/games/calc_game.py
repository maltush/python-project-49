import random


# Генерация выражения
# Возвращает два целых случайных числа, соединенных знаком +, -, *
def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    expression = f"{num1} {operation} {num2}"
    return expression


# Вычисление выражения
def calculate_answer(expression):
    return eval(expression)


# Игровое взаимодействие. Спрашиваем, сравниваем ответ с правильным
def play_game():
    print('What is the result of the expression?')

    for _ in range(3):  
        expression = generate_expression()
        print(f"Question: {expression}")
        user_answer = input('Your answer: ')

        correct_answer = calculate_answer(expression)

        if str(user_answer) != str(correct_answer):
            return False, correct_answer
        
        print("Correct!")

    return True, None 