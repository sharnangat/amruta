from flask import Flask, redirect, render_template, request, url_for
import sqlite3


app = Flask(__name__)
DB_NAME = "students_web.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
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


@app.route("/")
def index():
    with get_connection() as conn:
        students = conn.execute(
            "SELECT id, name, age, course FROM students ORDER BY id DESC"
        ).fetchall()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    course = request.form.get("course", "").strip()

    if name and age.isdigit() and course:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                (name, int(age), course),
            )
            conn.commit()

    return redirect(url_for("index"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
