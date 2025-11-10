
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine import run_game

def get_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer

def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(get_question_answer, rules, "even")

if __name__ == '__main__':
    main()
