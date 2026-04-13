"""
Pattern Printing Examples

A standalone Python program for practicing different printing patterns.
"""


def star_increasing(rows):
    for i in range(1, rows + 1):
        print("*" * i)


def star_decreasing(rows):
    for i in range(rows, 0, -1):
        print("*" * i)


def star_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def number_triangle(rows):
    for i in range(1, rows + 1):
        line = " ".join(str(j) for j in range(1, i + 1))
        print(line)


def number_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        line = " ".join(str(j) for j in range(1, i + 1))
        print(line)


def floyd_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        row_values = []
        for _ in range(i):
            row_values.append(str(num))
            num += 1
        print(" ".join(row_values))


def alphabet_triangle(rows):
    for i in range(1, rows + 1):
        line = " ".join(chr(64 + j) for j in range(1, i + 1))
        print(line)


def hollow_square(rows):
    if rows < 2:
        print("*")
        return
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("* " * rows)
        else:
            print("* " + "  " * (rows - 2) + "*")


def star_diamond(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    for i in range(rows - 1, 0, -1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def hollow_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "*")
        elif i == rows:
            print(spaces + "*" * (2 * rows - 1))
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")


def pascal_like_star(rows):
    for i in range(1, rows + 1):
        print("*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i)


def binary_triangle(rows):
    for i in range(1, rows + 1):
        line = []
        for j in range(1, i + 1):
            line.append(str((i + j) % 2))
        print(" ".join(line))


def number_palindrome_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        desc = "".join(str(j) for j in range(i, 0, -1))
        asc = "".join(str(j) for j in range(2, i + 1))
        print(spaces + desc + asc)


def butterfly_pattern(rows):
    for i in range(1, rows + 1):
        left = "*" * i
        middle = " " * (2 * (rows - i))
        right = "*" * i
        print(left + middle + right)
    for i in range(rows, 0, -1):
        left = "*" * i
        middle = " " * (2 * (rows - i))
        right = "*" * i
        print(left + middle + right)


def hollow_diamond(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "*")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")
    for i in range(rows - 1, 0, -1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "*")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")


def right_aligned_triangle(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        print(spaces + "*" * i)


def sandglass_star(rows):
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    for i in range(2, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def character_hourglass(rows):
    for i in range(rows, 0, -1):
        line = " ".join(chr(64 + j) for j in range(1, i + 1))
        print(line)
    for i in range(2, rows + 1):
        line = " ".join(chr(64 + j) for j in range(1, i + 1))
        print(line)


def checkerboard_pattern(rows):
    for i in range(rows):
        line = []
        for j in range(rows):
            if (i + j) % 2 == 0:
                line.append("*")
            else:
                line.append(" ")
        print(" ".join(line))


def zero_one_square(rows):
    for i in range(rows):
        line = []
        for j in range(rows):
            line.append(str((i + j) % 2))
        print(" ".join(line))


def show_menu():
    print("\n=== Pattern Printing Menu ===")
    print("1. Star Increasing Triangle")
    print("2. Star Decreasing Triangle")
    print("3. Star Pyramid")
    print("4. Number Triangle")
    print("5. Number Reverse Triangle")
    print("6. Floyd's Triangle")
    print("7. Alphabet Triangle")
    print("8. Hollow Square")
    print("9. Star Diamond")
    print("10. Hollow Pyramid")
    print("11. Pascal-like Star Pattern")
    print("12. Binary Triangle")
    print("13. Number Palindrome Pyramid")
    print("14. Butterfly Pattern")
    print("15. Hollow Diamond")
    print("16. Right Aligned Star Triangle")
    print("17. Sandglass Star Pattern")
    print("18. Character Hourglass")
    print("19. Checkerboard Star Pattern")
    print("20. 0-1 Square Pattern")
    print("21. Exit")


def main():
    print("Pattern Printing Program")
    while True:
        show_menu()
        choice = input("Enter choice (1-21): ").strip()

        if choice == "21":
            print("Goodbye!")
            break

        if choice not in {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
        }:
            print("Invalid choice. Please try again.")
            continue

        rows_input = input("Enter number of rows: ").strip()
        if not rows_input.isdigit() or int(rows_input) <= 0:
            print("Please enter a positive integer.")
            continue

        rows = int(rows_input)
        print()

        if choice == "1":
            star_increasing(rows)
        elif choice == "2":
            star_decreasing(rows)
        elif choice == "3":
            star_pyramid(rows)
        elif choice == "4":
            number_triangle(rows)
        elif choice == "5":
            number_reverse_triangle(rows)
        elif choice == "6":
            floyd_triangle(rows)
        elif choice == "7":
            alphabet_triangle(rows)
        elif choice == "8":
            hollow_square(rows)
        elif choice == "9":
            star_diamond(rows)
        elif choice == "10":
            hollow_pyramid(rows)
        elif choice == "11":
            pascal_like_star(rows)
        elif choice == "12":
            binary_triangle(rows)
        elif choice == "13":
            number_palindrome_pyramid(rows)
        elif choice == "14":
            butterfly_pattern(rows)
        elif choice == "15":
            hollow_diamond(rows)
        elif choice == "16":
            right_aligned_triangle(rows)
        elif choice == "17":
            sandglass_star(rows)
        elif choice == "18":
            character_hourglass(rows)
        elif choice == "19":
            checkerboard_pattern(rows)
        elif choice == "20":
            zero_one_square(rows)


if __name__ == "__main__":
    main()
