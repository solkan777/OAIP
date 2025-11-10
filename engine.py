#!/usr/bin/env python3

def run_game(get_question_answer, rules, game_name):
    print(f"VD-{game_name}")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)
    
    for i in range(3):
        question, correct_answer = get_question_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == str(correct_answer).lower():
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
