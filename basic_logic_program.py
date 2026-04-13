"""
Basic Python program for logic development.

Practice areas:
- Conditions (if/elif/else)
- Loops
- Functions
- Input handling
"""


def check_even_or_odd(number):
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


def max_of_three(a, b, c):
    """Return the largest of three numbers."""
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


def factorial(n):
    """Return factorial of n using a loop."""
    if n < 0:
        return None
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def main():
    print("=== Basic Logic Development Program ===")

    while True:
        print("\nChoose an option:")
        print("1. Check even or odd")
        print("2. Find largest of three numbers")
        print("3. Calculate factorial")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            num = int(input("Enter an integer: "))
            print(f"Result: {check_even_or_odd(num)}")

        elif choice == "2":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            print(f"Largest number: {max_of_three(a, b, c)}")

        elif choice == "3":
            n = int(input("Enter a non-negative integer: "))
            fact = factorial(n)
            if fact is None:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {n} is {fact}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
