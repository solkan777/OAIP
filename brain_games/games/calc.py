import random

def get_question_answer():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(operations)
    
    question = f"{num1} {operation} {num2}"
    
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    
    return question, str(correct_answer)

RULES = "What is the result of the expression?"
