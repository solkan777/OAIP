import random
import math

def main():
    print("VD-gcd")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        correct_answer = str(math.gcd(num1, num2))
 
        print(f"Question: {num1} {num2}")
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
