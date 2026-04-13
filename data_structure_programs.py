"""
Data Structure Programs in Python

Beginner-friendly menu-driven examples.
"""

from collections import deque


def stack_program():
    stack = []
    print("\nStack Program (LIFO)")
    while True:
        print("\n1. Push  2. Pop  3. Peek  4. Display  5. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = input("Enter value to push: ")
            stack.append(value)
            print("Pushed.")
        elif choice == "2":
            if stack:
                print(f"Popped: {stack.pop()}")
            else:
                print("Stack is empty.")
        elif choice == "3":
            if stack:
                print(f"Top element: {stack[-1]}")
            else:
                print("Stack is empty.")
        elif choice == "4":
            print(f"Stack: {stack}")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def queue_program():
    queue = deque()
    print("\nQueue Program (FIFO)")
    while True:
        print("\n1. Enqueue  2. Dequeue  3. Front  4. Display  5. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = input("Enter value to enqueue: ")
            queue.append(value)
            print("Enqueued.")
        elif choice == "2":
            if queue:
                print(f"Dequeued: {queue.popleft()}")
            else:
                print("Queue is empty.")
        elif choice == "3":
            if queue:
                print(f"Front element: {queue[0]}")
            else:
                print("Queue is empty.")
        elif choice == "4":
            print(f"Queue: {list(queue)}")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def linked_list_program():
    linked_list = []
    print("\nLinked List (using Python list for practice)")
    while True:
        print("\n1. Insert End  2. Insert At Position  3. Delete Value  4. Display  5. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = input("Enter value: ")
            linked_list.append(value)
            print("Inserted at end.")
        elif choice == "2":
            value = input("Enter value: ")
            pos = int(input("Enter position (0-based): "))
            if 0 <= pos <= len(linked_list):
                linked_list.insert(pos, value)
                print("Inserted.")
            else:
                print("Invalid position.")
        elif choice == "3":
            value = input("Enter value to delete: ")
            if value in linked_list:
                linked_list.remove(value)
                print("Deleted.")
            else:
                print("Value not found.")
        elif choice == "4":
            print("Linked List:", " -> ".join(linked_list) if linked_list else "Empty")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def searching_program():
    arr = [int(x) for x in input("Enter sorted integers: ").split()]
    target = int(input("Enter target: "))

    left, right = 0, len(arr) - 1
    found_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            found_index = mid
            break
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if found_index == -1:
        print("Element not found.")
    else:
        print(f"Element found at index {found_index}.")


def sorting_program():
    arr = [int(x) for x in input("Enter integers: ").split()]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f"Sorted array (selection sort): {arr}")


def hash_map_frequency_program():
    text = input("Enter text: ").strip().lower()
    freq = {}
    for ch in text:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    print("Character frequency:")
    for key in sorted(freq):
        print(f"{key} -> {freq[key]}")


def show_menu():
    print("\n=== Data Structure Programs Menu ===")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Linked List Operations")
    print("4. Binary Search")
    print("5. Selection Sort")
    print("6. Hash Map Frequency")
    print("7. Exit")


def main():
    print("Data Structure Practice Program")
    while True:
        show_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            stack_program()
        elif choice == "2":
            queue_program()
        elif choice == "3":
            linked_list_program()
        elif choice == "4":
            searching_program()
        elif choice == "5":
            sorting_program()
        elif choice == "6":
            hash_map_frequency_program()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
