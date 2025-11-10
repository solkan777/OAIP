
import random

def main():
    print("VD-even")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for i in range(3):
        number = random.randint(1, 100)
        correct_answer = "yes" if number % 2 == 0 else "no"
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
