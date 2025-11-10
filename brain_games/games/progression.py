import random

def get_question_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    return question, correct_answer

RULES = "What number is missing in the progression?"
