
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine import run_game

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer

def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(get_question_answer, rules, "prime")

if __name__ == '__main__':
    main()
