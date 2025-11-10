#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from engine import run_game
from brain_games.games import gcd

def main():
    run_game(gcd.get_question_answer, gcd.RULES, "gcd")

if __name__ == '__main__':
    main()
