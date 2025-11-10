
import random
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine import run_game

def get_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer

def main():
    rules = "Find the greatest common divisor of given numbers."
    run_game(get_question_answer, rules, "gcd")

if __name__ == '__main__':
    main()
