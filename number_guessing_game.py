"""
Number Guessing Game

A basic standalone Python program for logic development.
"""

import random


def play_game():
    print("=== Number Guessing Game ===")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ").strip()

        if not user_input.isdigit():
            print("Please enter a valid positive integer.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break


def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
