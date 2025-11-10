#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from engine import run_game
from brain_games.games import prime

def main():
    run_game(prime.get_question_answer, prime.RULES, "prime")

if __name__ == '__main__':
    main()
