# 🎓 Student Management System

A command-line interface (CLI) application developed in **Python** with an embedded **SQLite3** database for managing academic student records.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)](https://sqlite.org/)

---

## ✨ Features

- **Add Student Records:** Add student profiles with name and marks (`1. Add Student`).
- **View All Records:** Formatted tabular view of all stored student records (`2. View Students`).
- **Delete Student Record:** Remove records safely by unique student ID (`3. Delete Student`).
- **Persistent SQLite Storage:** Auto-initializes `students.db` table schema with auto-incrementing primary keys.
- **Interactive CLI Menu:** Loop-based console interface with input prompts and error handling.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite3 (standard library module)

---

## 📁 Project Structure

```text
student-management-system/
├── app.py          # CLI menu and SQLite database CRUD logic
├── README.md       # Project documentation
├── .gitignore      # Ignores runtime SQLite database & Python cache
└── students.db     # Local SQLite database (auto-created on first run)
```

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.8 or newer (no external dependencies required)

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/sujitha611/student-management-system.git
   cd student-management-system
   ```

2. Run the Python application:
   ```bash
   python app.py
   ```

3. Follow the on-screen menu:
   ```text
   1. Add Student
   2. View Students
   3. Delete Student
   4. Exit
   ```

---

## 👤 Developer
**Battu Jaya Sujitha**  
B.Tech in Computer Science and Engineering (Class of 2026)  
[GitHub Profile](https://github.com/sujitha611) | [LinkedIn](https://www.linkedin.com/in/jaya-sujitha-576b7a290/)
