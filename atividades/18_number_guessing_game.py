# Exercise 18: Number Guessing Game
import random

chosen_number = random.randint(1, 100)
print("Select a number between 1 and 100")
guesses = 0
is_running = True

while is_running:
    guess_number = input("Enter your guess: ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
        if guess_number < 1 or guess_number > 100:
            print("That number is out of range!")
            print("Please select a number between 1 and 100")
        else:
            guesses += 1
            if guess_number < chosen_number:
                print("Too low! Try again!")
            elif guess_number > chosen_number:
                print("Too high! Try again!")
            else:
                print(f"Correct! The answer was {chosen_number}")
                print(f"Number of guesses: {guesses}")
                is_running = False
    else:
        print("Invalid guess")
        print("Please select a number between 1 and 100")
