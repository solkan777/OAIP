
import random

def main():
    print("VD-progression")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    
    for i in range(3):
        
        length = random.randint(5, 10)
        start = random.randint(1, 50)
        step = random.randint(1, 10)
        
        progression = []
        for i in range(length):
            progression.append(str(start + i * step))
        
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."
        
        question = " ".join(progression)
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
