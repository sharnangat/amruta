"""
Array Programs in Python

A beginner-friendly, menu-driven program for array/list logic practice.
"""


def read_int_array():
    raw = input("Enter integers separated by space: ").strip()
    if not raw:
        return []
    return [int(value) for value in raw.split()]


def linear_search(arr, target):
    for idx, value in enumerate(arr):
        if value == target:
            return idx
    return -1


def find_min_max(arr):
    if not arr:
        return None, None
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum


def reverse_array(arr):
    return arr[::-1]


def bubble_sort(arr):
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def second_largest(arr):
    unique_values = sorted(set(arr), reverse=True)
    if len(unique_values) < 2:
        return None
    return unique_values[1]


def remove_duplicates(arr):
    seen = set()
    result = []
    for value in arr:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def left_rotate(arr, steps):
    if not arr:
        return []
    steps = steps % len(arr)
    return arr[steps:] + arr[:steps]


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


def frequency_count(arr):
    freq = {}
    for value in arr:
        freq[value] = freq.get(value, 0) + 1
    return freq


def show_menu():
    print("\n=== Array Programs Menu ===")
    print("1. Linear Search")
    print("2. Find Minimum and Maximum")
    print("3. Reverse Array")
    print("4. Bubble Sort")
    print("5. Second Largest Element")
    print("6. Remove Duplicates")
    print("7. Left Rotate Array")
    print("8. Merge Two Sorted Arrays")
    print("9. Frequency Count")
    print("10. Exit")


def main():
    print("Array Practice Program")

    while True:
        show_menu()
        choice = input("Enter choice (1-10): ").strip()

        if choice == "10":
            print("Goodbye!")
            break

        if choice == "1":
            arr = read_int_array()
            target = int(input("Enter target element: "))
            idx = linear_search(arr, target)
            if idx == -1:
                print("Element not found.")
            else:
                print(f"Element found at index {idx}.")

        elif choice == "2":
            arr = read_int_array()
            minimum, maximum = find_min_max(arr)
            if minimum is None:
                print("Array is empty.")
            else:
                print(f"Minimum: {minimum}, Maximum: {maximum}")

        elif choice == "3":
            arr = read_int_array()
            print(f"Reversed array: {reverse_array(arr)}")

        elif choice == "4":
            arr = read_int_array()
            print(f"Sorted array: {bubble_sort(arr)}")

        elif choice == "5":
            arr = read_int_array()
            result = second_largest(arr)
            if result is None:
                print("Second largest does not exist.")
            else:
                print(f"Second largest element: {result}")

        elif choice == "6":
            arr = read_int_array()
            print(f"Array after removing duplicates: {remove_duplicates(arr)}")

        elif choice == "7":
            arr = read_int_array()
            steps = int(input("Enter number of left rotations: "))
            print(f"Rotated array: {left_rotate(arr, steps)}")

        elif choice == "8":
            print("Enter first sorted array:")
            arr1 = read_int_array()
            print("Enter second sorted array:")
            arr2 = read_int_array()
            print(f"Merged sorted array: {merge_sorted_arrays(arr1, arr2)}")

        elif choice == "9":
            arr = read_int_array()
            freq = frequency_count(arr)
            if not freq:
                print("Array is empty.")
            else:
                print("Frequency of elements:")
                for key in sorted(freq):
                    print(f"{key} -> {freq[key]}")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
