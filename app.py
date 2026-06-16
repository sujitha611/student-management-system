import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER
    )
""")
conn.commit()

def add_student(name, marks):
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print("Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Student deleted!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        add_student(name, marks)
    elif choice == "2":
        view_students()
    elif choice == "3":
        id = int(input("Enter student ID: "))
        delete_student(id)
    elif choice == "4":
        break

conn.close()