# Exercise 19: Rock, Paper, Scissors
import random

options = ("rock", "paper", "scissors")
counter = {
    "wins": 0,
    "ties": 0,
    "losses": 0
}

while True:
    player = input("Enter a play (rock, paper, scissors) or q to quit: ").lower()

    if player == "q":
        print("------------------Final Result------------------")
        for result, count in counter.items():
            print(f"{result}: {count}")
        break

    if player not in options:
        print("Invalid option, try again!")
        continue

    computer = random.choice(options)
    print(f"{player} x {computer}")

    if player == computer:
        print("It's a tie!")
        counter["ties"] += 1
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            counter["wins"] += 1
        elif computer == "paper":
            print("You lose!")
            counter["losses"] += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            counter["wins"] += 1
        elif computer == "scissors":
            print("You lose!")
            counter["losses"] += 1
    else:
        if computer == "paper":
            print("You win!")
            counter["wins"] += 1
        elif computer == "rock":
            print("You lose!")
            counter["losses"] += 1