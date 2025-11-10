#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from engine import run_game
from brain_games.games import progression

def main():
    run_game(progression.get_question_answer, progression.RULES, "progression")

if __name__ == '__main__':
    main()
