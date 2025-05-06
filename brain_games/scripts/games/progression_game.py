import random


# Создает прогрессию 
def generate_progression(length=10):
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    progression = [start + step * i for i in range(length)]
    return progression


# Заменяет символ на две точки
def hide_number(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_number


# Игровое взаимодействие. Создаем прогрессию со спрятанным элементом, спрашиваем, сравниваем ответ с правильным
def play_game():
    print("What number is missing in the progression?")

    for _ in range(3): 
        progression_length = random.randint(5, 10)
        progression = generate_progression(progression_length)
        hidden_progression, hidden_number = hide_number(progression)
        
        print("Question:", ' '.join(map(str, hidden_progression)))
        user_answer = input("Your answer: ")
        
        if str(user_answer) != str(hidden_number):
            return False, hidden_number
        
        print("Correct!")

    return True, None 


