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


def is_prime(number):
    """Return True if number is prime, else False."""
    if number < 2:
        return False
    for value in range(2, int(number ** 0.5) + 1):
        if number % value == 0:
            return False
    return True


def reverse_number(number):
    """Return the reversed form of an integer."""
    sign = -1 if number < 0 else 1
    reversed_str = str(abs(number))[::-1]
    return sign * int(reversed_str)


def sum_of_digits(number):
    """Return sum of digits in an integer."""
    return sum(int(ch) for ch in str(abs(number)))


def fibonacci_series(count):
    """Return first 'count' Fibonacci numbers as a list."""
    if count <= 0:
        return []
    if count == 1:
        return [0]
    series = [0, 1]
    while len(series) < count:
        series.append(series[-1] + series[-2])
    return series


def is_palindrome_text(text):
    """Check if given text is a palindrome (ignoring case/spaces)."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def multiplication_table(number, limit=10):
    """Return multiplication table lines for a number up to limit."""
    lines = []
    for value in range(1, limit + 1):
        lines.append(f"{number} x {value} = {number * value}")
    return lines


def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_armstrong(number):
    """Check whether a number is an Armstrong number."""
    digits = str(abs(number))
    power = len(digits)
    total = sum(int(ch) ** power for ch in digits)
    return total == abs(number)


def count_vowels(text):
    """Return number of vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)


def day_name_from_number(day_number):
    """Return day name for 1-7 using match-case."""
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"


def simple_calculator_match(first, operator, second):
    """Return calculator result using match-case operators."""
    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            if second == 0:
                return "Cannot divide by zero"
            return first / second
        case _:
            return "Invalid operator"


def grade_message(score):
    """Return grade message using match-case with guards."""
    match score:
        case s if 90 <= s <= 100:
            return "Grade A"
        case s if 75 <= s < 90:
            return "Grade B"
        case s if 60 <= s < 75:
            return "Grade C"
        case s if 0 <= s < 60:
            return "Needs Improvement"
        case _:
            return "Invalid score"


def star_patterns(rows, pattern_type):
    """Return star pattern lines based on selected type."""
    lines = []

    if pattern_type == "1":
        for i in range(1, rows + 1):
            lines.append("*" * i)
    elif pattern_type == "2":
        for i in range(rows, 0, -1):
            lines.append("*" * i)
    elif pattern_type == "3":
        for i in range(1, rows + 1):
            spaces = " " * (rows - i)
            stars = "*" * (2 * i - 1)
            lines.append(spaces + stars)
    elif pattern_type == "4":
        for i in range(1, rows + 1):
            left = "*" * i
            right = "*" * i
            middle = " " * (2 * (rows - i))
            lines.append(left + middle + right)
    else:
        lines.append("Invalid pattern type")

    return lines


def main():
    print("=== Basic Logic Development Program ===")

    while True:
        print("\nChoose an option:")
        print("1. Check even or odd")
        print("2. Find largest of three numbers")
        print("3. Calculate factorial")
        print("4. Check prime number")
        print("5. Reverse a number")
        print("6. Sum of digits")
        print("7. Generate Fibonacci series")
        print("8. Palindrome check (text)")
        print("9. Multiplication table")
        print("10. GCD of two numbers")
        print("11. LCM of two numbers")
        print("12. Armstrong number check")
        print("13. Count vowels in text")
        print("14. Switch example: day from number")
        print("15. Switch example: simple calculator")
        print("16. Switch example: grade message")
        print("17. * printing patterns")
        print("18. Exit")

        choice = input("Enter choice (1-18): ").strip()

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
            num = int(input("Enter an integer: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")

        elif choice == "5":
            num = int(input("Enter an integer: "))
            print(f"Reversed number: {reverse_number(num)}")

        elif choice == "6":
            num = int(input("Enter an integer: "))
            print(f"Sum of digits: {sum_of_digits(num)}")

        elif choice == "7":
            count = int(input("How many Fibonacci terms do you want? "))
            series = fibonacci_series(count)
            if not series:
                print("Please enter a positive count.")
            else:
                print(f"Fibonacci series ({count} terms): {series}")

        elif choice == "8":
            text = input("Enter text: ")
            if is_palindrome_text(text):
                print("It is a palindrome.")
            else:
                print("It is not a palindrome.")

        elif choice == "9":
            num = int(input("Enter a number: "))
            limit = int(input("Enter table limit (default 10 suggested): "))
            for line in multiplication_table(num, limit):
                print(line)

        elif choice == "10":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            print(f"GCD({a}, {b}) = {gcd(a, b)}")

        elif choice == "11":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            print(f"LCM({a}, {b}) = {lcm(a, b)}")

        elif choice == "12":
            num = int(input("Enter an integer: "))
            if is_armstrong(num):
                print(f"{num} is an Armstrong number.")
            else:
                print(f"{num} is not an Armstrong number.")

        elif choice == "13":
            text = input("Enter text: ")
            print(f"Number of vowels: {count_vowels(text)}")

        elif choice == "14":
            day_number = int(input("Enter day number (1-7): "))
            print(day_name_from_number(day_number))

        elif choice == "15":
            first = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            second = float(input("Enter second number: "))
            print(f"Result: {simple_calculator_match(first, operator, second)}")

        elif choice == "16":
            score = int(input("Enter score (0-100): "))
            print(grade_message(score))

        elif choice == "17":
            rows = int(input("Enter number of rows: "))
            print("Choose star pattern:")
            print("1. Increasing triangle")
            print("2. Decreasing triangle")
            print("3. Pyramid")
            print("4. Butterfly")
            pattern_type = input("Enter pattern choice (1-4): ").strip()
            for line in star_patterns(rows, pattern_type):
                print(line)

        elif choice == "18":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
