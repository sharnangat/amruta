"""
Database Program in Python (SQLite)

A simple CRUD application for managing student records.
"""

import sqlite3


DB_NAME = "students.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL
            )
            """
        )
        conn.commit()


def add_student():
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: ").strip())
    course = input("Enter course name: ").strip()

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course),
        )
        conn.commit()
    print("Student added successfully.")


def view_students():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, course FROM students ORDER BY id")
        rows = cursor.fetchall()

    if not rows:
        print("No student records found.")
        return

    print("\nID | Name | Age | Course")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def update_student():
    student_id = int(input("Enter student ID to update: ").strip())
    name = input("Enter new name: ").strip()
    age = int(input("Enter new age: ").strip())
    course = input("Enter new course: ").strip()

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
            (name, age, course, student_id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            print("Student updated successfully.")


def delete_student():
    student_id = int(input("Enter student ID to delete: ").strip())

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            print("Student deleted successfully.")


def show_menu():
    print("\n=== Database Program Menu ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


def main():
    create_table()
    print("SQLite Student Database Program")

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
