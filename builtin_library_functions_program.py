"""
Python Built-in/Standard Library Functions Demo

Menu-driven examples using common Python library modules.
"""

import math
import random
import statistics
from datetime import datetime, timedelta
from itertools import permutations
from collections import Counter


def math_examples():
    num = float(input("Enter a number: "))
    print(f"sqrt({num}) = {math.sqrt(num) if num >= 0 else 'not defined for negative'}")
    print(f"ceil({num}) = {math.ceil(num)}")
    print(f"floor({num}) = {math.floor(num)}")
    print(f"factorial(5) = {math.factorial(5)}")
    print(f"pow(2, 5) = {math.pow(2, 5)}")


def statistics_examples():
    values = input("Enter numbers separated by space: ").strip().split()
    data = [float(v) for v in values]
    if not data:
        print("No data provided.")
        return
    print(f"Mean = {statistics.mean(data)}")
    print(f"Median = {statistics.median(data)}")
    if len(data) > 1:
        print(f"Standard Deviation = {statistics.stdev(data)}")
    else:
        print("Standard Deviation needs at least 2 values.")


def random_examples():
    print(f"Random integer (1-100): {random.randint(1, 100)}")
    sample = [10, 20, 30, 40, 50]
    print(f"Random choice from {sample}: {random.choice(sample)}")
    random.shuffle(sample)
    print(f"Shuffled list: {sample}")


def datetime_examples():
    now = datetime.now()
    print(f"Current date/time: {now}")
    print(f"Formatted: {now.strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"After 7 days: {now + timedelta(days=7)}")
    print(f"Before 30 days: {now - timedelta(days=30)}")


def itertools_examples():
    text = input("Enter text (max 4 chars suggested): ").strip()
    if not text:
        print("No text provided.")
        return
    perms = list(permutations(text))
    print(f"Total permutations: {len(perms)}")
    print("First 10 permutations:")
    for item in perms[:10]:
        print("".join(item))


def collections_examples():
    text = input("Enter text: ").strip()
    counter = Counter(text.replace(" ", "").lower())
    print("Character counts:")
    for key, value in sorted(counter.items()):
        print(f"{key} -> {value}")


def show_menu():
    print("\n=== Built-in Library Functions Menu ===")
    print("1. math module examples")
    print("2. statistics module examples")
    print("3. random module examples")
    print("4. datetime module examples")
    print("5. itertools module examples")
    print("6. collections module examples")
    print("7. Exit")


def main():
    print("Python Library Functions Practice Program")

    while True:
        show_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            math_examples()
        elif choice == "2":
            statistics_examples()
        elif choice == "3":
            random_examples()
        elif choice == "4":
            datetime_examples()
        elif choice == "5":
            itertools_examples()
        elif choice == "6":
            collections_examples()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
