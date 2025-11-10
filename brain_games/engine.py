
import prompt

def run_game(game_module):
    print(f"VD-{game_module.GAME_NAME}")
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    
    print(game_module.RULES)
    
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
