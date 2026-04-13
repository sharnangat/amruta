"""
2D, 3D, and Multi-Dimensional Array Programs in Python
"""


def input_2d_matrix(rows, cols, name="Matrix"):
    print(f"Enter values for {name} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_values = input(f"Row {i + 1}: ").strip().split()
            if len(row_values) != cols:
                print(f"Please enter exactly {cols} values.")
                continue
            matrix.append([int(value) for value in row_values])
            break
    return matrix


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(str(value) for value in row))


def add_2d_matrices():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    a = input_2d_matrix(rows, cols, "Matrix A")
    b = input_2d_matrix(rows, cols, "Matrix B")

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    print_matrix(result, "A + B")


def transpose_2d_matrix():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    matrix = input_2d_matrix(rows, cols)

    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)

    print_matrix(matrix, "Original Matrix")
    print_matrix(transposed, "Transposed Matrix")


def multiply_2d_matrices():
    r1 = int(input("Enter rows of Matrix A: "))
    c1 = int(input("Enter cols of Matrix A: "))
    r2 = int(input("Enter rows of Matrix B: "))
    c2 = int(input("Enter cols of Matrix B: "))

    if c1 != r2:
        print("Matrix multiplication not possible (c1 must equal r2).")
        return

    a = input_2d_matrix(r1, c1, "Matrix A")
    b = input_2d_matrix(r2, c2, "Matrix B")

    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)

    print_matrix(result, "A x B")


def diagonal_sum_2d():
    n = int(input("Enter size of square matrix (n): "))
    matrix = input_2d_matrix(n, n)

    primary = 0
    secondary = 0
    for i in range(n):
        primary += matrix[i][i]
        secondary += matrix[i][n - i - 1]

    print_matrix(matrix, "Square Matrix")
    print(f"Primary diagonal sum: {primary}")
    print(f"Secondary diagonal sum: {secondary}")


def create_3d_array():
    x = int(input("Enter size for dimension X: "))
    y = int(input("Enter size for dimension Y: "))
    z = int(input("Enter size for dimension Z: "))

    value = 1
    arr = []
    for i in range(x):
        plane = []
        for j in range(y):
            row = []
            for _ in range(z):
                row.append(value)
                value += 1
            plane.append(row)
        arr.append(plane)

    print("\nGenerated 3D Array:")
    for i in range(x):
        print(f"Layer {i + 1}:")
        for row in arr[i]:
            print(row)


def sum_all_elements_3d():
    x = int(input("Enter size for dimension X: "))
    y = int(input("Enter size for dimension Y: "))
    z = int(input("Enter size for dimension Z: "))

    print("Enter values for 3D array:")
    arr = []
    total_sum = 0
    for i in range(x):
        plane = []
        print(f"Layer {i + 1}:")
        for j in range(y):
            while True:
                values = input(f"Row {j + 1} ({z} values): ").strip().split()
                if len(values) != z:
                    print(f"Please enter exactly {z} values.")
                    continue
                row = [int(value) for value in values]
                total_sum += sum(row)
                plane.append(row)
                break
        arr.append(plane)

    print(f"Sum of all elements in 3D array: {total_sum}")


def flatten_multidimensional():
    data = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]],
    ]

    flat = []
    for plane in data:
        for row in plane:
            for value in row:
                flat.append(value)

    print("Sample 3D array:", data)
    print("Flattened array:", flat)


def show_menu():
    print("\n=== Multi-Dimensional Array Programs ===")
    print("1. Add Two 2D Matrices")
    print("2. Transpose a 2D Matrix")
    print("3. Multiply Two 2D Matrices")
    print("4. Diagonal Sum of 2D Square Matrix")
    print("5. Create and Display a 3D Array")
    print("6. Sum All Elements in a 3D Array")
    print("7. Flatten a Multi-Dimensional Array")
    print("8. Exit")


def main():
    print("2D, 3D, and Multi-Dimensional Array Practice")

    while True:
        show_menu()
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            add_2d_matrices()
        elif choice == "2":
            transpose_2d_matrix()
        elif choice == "3":
            multiply_2d_matrices()
        elif choice == "4":
            diagonal_sum_2d()
        elif choice == "5":
            create_3d_array()
        elif choice == "6":
            sum_all_elements_3d()
        elif choice == "7":
            flatten_multidimensional()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
