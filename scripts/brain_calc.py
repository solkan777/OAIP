#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from engine import run_game
from brain_games.games import calc

def main():
    run_game(calc.get_question_answer, calc.RULES, "calc")

if __name__ == '__main__':
    main()
