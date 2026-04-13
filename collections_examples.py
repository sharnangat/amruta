"""
collections module examples in Python
"""

from collections import Counter, defaultdict, deque, namedtuple


def counter_example():
    text = input("Enter text: ").strip().lower().replace(" ", "")
    counts = Counter(text)
    print("Character frequency using Counter:")
    for ch, count in sorted(counts.items()):
        print(f"{ch} -> {count}")


def defaultdict_example():
    pairs = [("math", 90), ("science", 85), ("math", 88), ("english", 92)]
    grouped = defaultdict(list)
    for subject, marks in pairs:
        grouped[subject].append(marks)

    print("Grouped marks using defaultdict(list):")
    for subject in sorted(grouped):
        print(f"{subject}: {grouped[subject]}")


def deque_example():
    dq = deque([10, 20, 30])
    print(f"Initial deque: {list(dq)}")
    dq.append(40)
    dq.appendleft(5)
    print(f"After append/appendleft: {list(dq)}")
    dq.pop()
    dq.popleft()
    print(f"After pop/popleft: {list(dq)}")


def namedtuple_example():
    Student = namedtuple("Student", ["name", "age", "course"])
    s1 = Student("Amruta", 21, "Python")
    print("namedtuple example:")
    print(f"Name: {s1.name}, Age: {s1.age}, Course: {s1.course}")


def show_menu():
    print("\n=== collections Examples Menu ===")
    print("1. Counter example")
    print("2. defaultdict example")
    print("3. deque example")
    print("4. namedtuple example")
    print("5. Exit")


def main():
    print("collections Module Practice Program")
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            counter_example()
        elif choice == "2":
            defaultdict_example()
        elif choice == "3":
            deque_example()
        elif choice == "4":
            namedtuple_example()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
