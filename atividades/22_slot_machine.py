# Exercise 22: Slot Machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
    else:
        return 0

def main():
    balance = 100

    print("----------------------------------------")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print("----------------------------------------")
        print(f"Current balance: ${balance:.2f}")

        bet = input("Place you bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid bet amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance for this bet.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("----------------------------------------")
        print("Spinning...")

        print_row(row)

        payout = get_payout(row, bet)

        print("----------------------------------------")
        if payout > 0:
            
            print(f"You won ${payout:.2f}!")
        else:
            print("You lost this round.")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.upper() != "Y":
            break

    print("Thank you for playing!")
    print(f"Your final balance is: ${balance:.2f}")

if __name__ == "__main__":
    main()